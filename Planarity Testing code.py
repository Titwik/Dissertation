# code to test planarity of graphs
# do this by checking if there exists a subgraph of the graph G that is a 
# K_5 graph or a K_(3,3) graph

# ALTERNATIVELY
# Use nx.is_planar(G) to check whether the graph is planar.
# It returns a boolean 'True' or 'False' if it is or isn't

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Make a graph
G = nx.complete_graph(5)
G.add_edge(1,5)
G.add_edge(5,2)
G.add_edge(2,6)
nx.draw_networkx(G, node_color="w", edgecolors="k")
plt.title('Graph of G')
plt.show()

H = nx.complete_graph(4)
nx.draw_networkx(H, node_color="w", edgecolors="k")
plt.title('Graph of H')
plt.show()

print('Is G planar?', nx.is_planar(G))
print('Is H planar?', nx.is_planar(H))