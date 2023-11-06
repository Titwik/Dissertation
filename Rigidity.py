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
random.seed(45)

####################################################################################################
# isomorphism checking code
def check_isomorphism(Graphs):
    for i in range(len(Graphs)):
        for j in range(len(Graphs)):    
            if nx.is_isomorphic(Graphs[i], Graphs[j]) == True and i != j:
                print(f'Graphs G{i+1} and G{j+1} are isomorphic')

####################################################################################################
# planarity checking code
def check_planarity(G):
    is_planar, G_example = nx.check_planarity(G)
    if is_planar == False:
        return False

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
# check for inf rigidity as this implies rigidity

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
            return True
        else:
            return False
            
    elif n  <= d + 1:
        if R_rank == math.comb(n, 2):
            return True
        else:
            return False
    else:
        return False

####################################################################################################

# Examples of planar and minimally rigid
# Minimally rigid graphs have 2n-3 edges, where n is number of nodes

# number of vertices
v = 8

# load all graphs on 8 vertices and 13 edges
Graphs_8 = nx.read_graph6("C:/Users/amrit/Desktop/University/Python/Diss Work/planar-8-13.g6")

# filter out the graphs that have degree 2 vertices
graphs_without_degree_2 = []

for i in range(len(Graphs_8)):
    
    G = Graphs_8[i]
    has_low_degree = False
    
    for j in range(8):
        if len(list(G[j])) <= 2:
            has_low_degree = True
            break
        
    if has_low_degree == False:
        graphs_without_degree_2.append(G)
            
# identify rigid graphs
# 17 rigid graphs on 8 vertices and 13 edges without degree 2 vertices
rigid_graphs_8 = []   

for i in range(len(graphs_without_degree_2)):
    
    G = graphs_without_degree_2[i]
    
    if check_rigidity(G) == True:
        rigid_graphs_8.append(G)

print(f'There are {len(rigid_graphs_8)} rigid graphs for n = 8 and e = 13')

####################################################################################################

# number of vertices
v = 9

# load all graphs on 9 vertices and 15 edges
Graphs_9 = nx.read_graph6("C:/Users/amrit/Desktop/University/Python/Diss Work/planar-9-15.g6")

# filter out the graphs that have degree 2 vertices
graphs_without_degree_2 = []

for i in range(len(Graphs_9)):
    
    G = Graphs_9[i]
    has_low_degree = False
    
    for j in range(v):
        if len(list(G[j])) <= 2:
            has_low_degree = True
            break
        
    if has_low_degree == False:
        graphs_without_degree_2.append(G)

# identify rigid graphs
# 111 rigid graphs on 9 vertices and 15 edges without degree 2 vertices
rigid_graphs_9 = []   

for i in range(len(graphs_without_degree_2)):
    G = graphs_without_degree_2[i]
    if check_rigidity(G) == True:
        rigid_graphs_9.append(G)

print(f'There are {len(rigid_graphs_9)} rigid graphs for n = 9 and e = 15')

####################################################################################################

# number of vertices
v = 10

# load all graphs on 10 vertices and 17 edges
Graphs_10 = nx.read_graph6("C:/Users/amrit/Desktop/University/Python/Diss Work/planar-10-17.g6")

# filter out the graphs that have degree 2 vertices
graphs_without_degree_2 = []

for i in range(len(Graphs_10)):
    
    G = Graphs_10[i]
    has_low_degree = False
    
    for j in range(v):
        if len(list(G[j])) <= 2:
            has_low_degree = True
            break
        
    if has_low_degree == False:
        graphs_without_degree_2.append(G)

# identify rigid graphs
# 926 rigid graphs on 10 vertices and 17 edges without degree 2 vertices
rigid_graphs_10 = []   

for i in range(len(graphs_without_degree_2)):
    G = graphs_without_degree_2[i]
    if check_rigidity(G) == True:
        rigid_graphs_10.append(G)

print(f'There are {len(rigid_graphs_10)} rigid graphs for n = 10 and e = 17')
    
nx.draw_planar(rigid_graphs_10[103])
plt.show()






















