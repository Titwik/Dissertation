# Code to test the rigidity of a graph
# plan is to create a networkx graph and then, for each node, randomly assign 
# a point onto the x-y plane so that it can be analysed
# use seed to ensure reproducibility 

# import relevant modules
import math
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# set the seed for reproducibility
#random.seed(45)

####################################################################################################

# create a graph first
G = nx.Graph()
G.add_edge(0, 1)
G.add_edge(0,3)
G.add_edge(2, 1)
G.add_edge(2,3)
nx.draw_networkx(G)

####################################################################################################

# create a function that plots the graph on the x-y plane
def G_coordinates(G):
    num_of_nodes = len(G.nodes)
    x_nodes = []
    y_nodes = []
    
    # create random coordinates for each node in the graph
    for i in range(num_of_nodes):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        x_nodes.append(x)
        y_nodes.append(y)
    
    # JUST SAYING
    # THE STUFF BELOW THIS ISN'T REALLY NECESSARY
    # IT'S JUST TO HELP VISUALIZE
    
    ############################
    # Plot the graph
    #plt.figure()
    
    # Plot the nodes onto the graph
    #plt.plot(x_nodes, y_nodes, 'bo', markersize=15)
    
    # Add labels to the points
    #for i, (x, y) in enumerate(zip(x_nodes, y_nodes)):
    #    plt.text(x, y, str(i), fontsize=12, ha='center', va='center', color='white')
    
    # Add the edges between the corresponding nodes
    #edges = list(G.edges)
    #for i in range(len(edges)):
    #    point_1 = [x_nodes[edges[i][0]], x_nodes[edges[i][1]]]
    #    point_2 = [y_nodes[edges[i][0]], y_nodes[edges[i][1]]]
    #    plt.plot(point_1, point_2, 'k-')
    
    #plt.show()
    ############################
    
    return x_nodes, y_nodes

####################################################################################################

# create the rigidity matrix

# create a matrix that is n row and d*n columns
# only consider d = 2 for now
def rigidity_matrix(G):
    
    # extract the coordinates of the graph
    x_nodes, y_nodes = G_coordinates(G)
    
    n = len(G.nodes())
    m = len(G.edges())

    # initialise the rigidity matrix
    R = np.zeros((m, 2*n))
    
    # compute the entries of the matrix
    for i, (u, v) in enumerate(G.edges()):
        xu, yu = x_nodes[u], y_nodes[u]
        xv, yv = x_nodes[v], y_nodes[v]

        # each row represents a specific edge
        # each column represents the difference in each coordinate of that edge
        R[i, 2 * u] = xu - xv
        R[i, 2 * u + 1] = yu - yv
        
        R[i, 2 * v] = xv - xu
        R[i, 2 * v + 1] = yv - yu

    return R

####################################################################################################

# create the criteria for rigidity
# A generic framework is rigid iff it is infinitesimally rigid
# CHECK TO SEE GRAPH IS GENERIC???

def check_rigidity(G):
    
    # number of nodes
    n = len(G.nodes())
    
    # working in dimension 2 so
    d = 2
    
    # find the rigidity matrix of G
    R = rigidity_matrix(G)
    
    # find the rank of R
    R_rank = np.linalg.matrix_rank(R)
    
    # check whether the rank satsifies Infinitesimal rigidity condition
    if n >= d + 2:
        if R_rank == d * n - math.comb(d+1, 2):
            print('Framework is rigid')
        else:
            print('Framework is flexible')
    elif n  <= d + 1:
        if R_rank == math.comb(n, 2):
            print('Framework is Rigid')
        else:
            print('Framework is flexible')
    else:
        print('Framework is flexible')

check_rigidity(G)
            
            
            
    


























    