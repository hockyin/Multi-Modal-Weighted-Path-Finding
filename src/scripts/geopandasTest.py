import geopandas as gpd
import matplotlib.pyplot as plt
import shapely
import networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors

ox.config(use_cache=True, log_console=True)
ox.__version__
# get a graph for some city
G = ox.graph_from_place('Munich, Bavaria, Germany', network_type='bike')
fig, ax = ox.plot_graph(G)

# gdf = gpd.read_file("C:/Users/BladeRunner/Downloads/oberbayern-latest-free.shp/"
#                                   "gis_osm_buildings_a_free_1.shp")

# print(gdf.shape)
# print(gdf.head())
# gdf.plot(figsize=(5,5), edgecolor="purple", facecolor="None")
# plt.show()

