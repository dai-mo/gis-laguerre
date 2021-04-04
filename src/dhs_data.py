import geopandas as gpd
import fiona
import itertools
import numpy as np


class DHSGeographicData():
    """Class representing the DHS geographic dataset
    """

    def __init__(self, filename: str):
        try:
            self.country_gdf = gpd.read_file(filename)
        except fiona.errors.DataIOError as err:
            raise TypeError

    def clean(self):
        """Drops all rows with longitude = 0.0 and latitude = 0.0 as they are not valid for land data.
        """
        self.country_cleaned_gdf = self.country_gdf.loc[(
            self.country_gdf['LATNUM'] != 0.0) & (self.country_gdf['LONGNUM'] != 0.0)]

    def extract_dhs(self):
        """Extract only the necessary columns from the cleaned geodataframe
        """
        self.country_extracted_gdf = self.country_cleaned_gdf[[
            'DHSID', 'DHSCLUST', 'ADM1DHS', 'DHSREGCO', 'DHSREGNA', 'URBAN_RURA', 'LATNUM', 'LONGNUM', 'ALT_DEM', 'DATUM', 'geometry']]

    def get_sites_and_radii(self):
        """Prepare country_extracted geodataframe for voronoi cell computation. 
        """
        # Add another column to country_extracted_gdf to represent the weights for weighted voronoi computation.
        # Using the approximate formula where 1 degree Latitude = 111 km we have:
        # 2 km = 0.018018 degrees and 5 km = 0.045045 degrees.
        self.country_extracted_gdf['WEIGHT'] = [
            0.018018 if x == 'U' else 0.045045 for x in self.country_extracted_gdf['URBAN_RURA']]

        # extract all the points as list from geoseries
        coords = self.country_extracted_gdf.geometry.apply(
            self.coord_lister_of_point_series)
        npcoord = coords.to_numpy()
        merged = list(itertools.chain(*npcoord))
        sites_list = [list(elem) for elem in merged]
        npsites = np.array([np.array(si) for si in sites_list])

        # extract all weights as list from panda.coreseries
        weights = self.country_extracted_gdf.WEIGHT
        weights_list = weights.to_list()
        npweights = np.array(weights_list)

        return (npsites, npweights)

    def coord_lister_of_point_series(self, geom):
        coords = list(geom.coords)
        return (coords)
