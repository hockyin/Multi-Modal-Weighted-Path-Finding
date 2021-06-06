import geopandas as gpd
import matplotlib.pyplot as plt
import shapely
import networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors
import peartree as pt
import os
from MMWPF import src
import sys

print(sys.path)
print(maps.path)

# gftsPath = (os.getcwd().rsplit(os.sep,1)[0] + os.sep + 'maps' + os.sep + 'mvv_gtfs.zip')
# print(gftsPath)
#
# # Automatically identify the busiest day and
# # read that in as a Partidge feed
# feed = pt.get_representative_feed(gftsPath)
#
# # Set a target time period to
# # use to summarize impedance
# start = 7*60*60  # 7:00 AM
# end = 10*60*60  # 10:00 AM
#
# # Converts feed subset into a directed
# # network multigraph
# G = pt.load_feed_as_graph(feed, start, end)
# fig, ax = ox.plot_graph(G)
# pt.plot.generate_plot(G)
