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
    dhs_geo_data.combine_dhs_voronoi(poly_lst)

    # Write to files
    # write to csv
    dhs_geo_data.ctry_dhs_weighted_voronoi.to_csv(os.environ.get(
        "OUT_DIR") + "/IAGE71FL_Voronoi.csv")

    # write to shapefile
    dhs_geo_data.ctry_dhs_weighted_voronoi.to_file(os.environ.get(
        "OUT_DIR") + "/IAGE71FL_Voronoi.shp")


if __name__ == "__main__":
    main()
