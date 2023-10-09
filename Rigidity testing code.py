# Code to test the rigidity of a graph
# plan is to create a networkx graph and then, for each node, randomly assign 
# a point onto the x-y plane so that it can be analysed
# use seed to ensure reproducibility 

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

# set the seed for reproducibility
random.seed(42)

####################################################################################################

# create a graph first
G = nx.complete_graph(5)
G.add_edge(2,5)
nx.draw_networkx(G)

####################################################################################################

# create a function that plots the graph on the x-y plane
def G_plane(G):
    num_of_nodes = len(G.nodes)
    x_nodes = []
    y_nodes = []
    
    # create random coordinates for each node in the graph
    for i in range(num_of_nodes):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        x_nodes.append(x)
        y_nodes.append(y)
    
    # Plot the graph
    plt.figure()
    
    # Plot the nodes onto the graph
    plt.plot(x_nodes, y_nodes, 'bo', markersize=15)
    
    # Add labels to the points
    for i, (x, y) in enumerate(zip(x_nodes, y_nodes)):
        plt.text(x, y, str(i), fontsize=12, ha='center', va='center', color='white')
    
    # Add the edges between the corresponding nodes
    edges = list(G.edges)
    for i in range(len(edges)):
        point_1 = [x_nodes[edges[i][0]], x_nodes[edges[i][1]]]
        point_2 = [y_nodes[edges[i][0]], y_nodes[edges[i][1]]]
        plt.plot(point_1, point_2, 'k-')
    
    plt.show()

    
G_plane(G)
