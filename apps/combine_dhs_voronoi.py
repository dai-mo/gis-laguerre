import multiprocessing as mp
import matplotlib.pyplot as plt
import laguerre_voronoi_2d as lv2d
import sys
import os
from dotenv import load_dotenv
import numpy as np
from joblib import Parallel, delayed
from tqdm import tqdm

import src.dhs_data as dd
load_dotenv()


def main():
    dhs_geo_file = os.environ.get(
        "DHS_DATA_DIR") + "/IAGE71FL_geographic_data/IAGE71FL.shp"
    dhs_geo_data = dd.DHSGeographicData(dhs_geo_file)
    dhs_geo_data.clean()
    dhs_geo_data.extract_dhs()

    (sites, weights) = dhs_geo_data.get_sites_and_radii()
    # Compute the power triangulation of the circles
    tri_list, vor_vert = lv2d.get_power_triangulation(sites, weights)
    # Compute the Voronoi cells
    voronoi_cell_map = lv2d.get_voronoi_cells(sites, vor_vert, tri_list)
    # Compute voronoi polygonal list
    poly_lst = dhs_geo_data.get_shapely_polygons(voronoi_cell_map)
    # Combine
    country_dhs_voronoi_gdf = dhs_geo_data.country_extracted_gdf
    country_dhs_voronoi_gdf = country_dhs_voronoi_gdf.reindex(
        columns=['DHSID', 'DHSCLUST', 'DHSREGNA', 'URBAN_RURA', 'LATNUM', 'LONGNUM', 'DATUM', 'geometry', 'cells'])
    country_dhs_voronoi_gdf['cells'] = 0
    manager = mp.Manager()
    voronois = manager.list(np.zeros(country_dhs_voronoi_gdf.shape[0]))

    def processInput(i):
        pt = country_dhs_voronoi_gdf.loc[i, 'geometry']
        for poly in poly_lst:
            if poly.contains(pt):
                if voronois[i] == 0:
                    voronois[i] = poly
                    return i
                else:
                    print("cell not empty.")

    num_cores = mp.cpu_count()
    p = country_dhs_voronoi_gdf.shape[0]
    inputs = range(p)
    results = Parallel(n_jobs=num_cores)(delayed(processInput)(i)
                                         for i in tqdm(inputs))

    # Add voronois list to dataframe cell
    country_dhs_voronoi_gdf['cells'] = voronois

    # Write to files
    # write to csv
    dhs_geo_data.country_voronoi_gdf.to_csv(os.environ.get(
        "OUT_DIR") + "/india_dhs_weighted_voronoi.csv")

    # write to shapefile
    dhs_geo_data.country_voronoi_gdf.to_file(os.environ.get(
        "OUT_DIR") + "/india_dhs_weighted_voronoi.shp")


if __name__ == "__main__":
    main()
