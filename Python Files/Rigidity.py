# Code to test the rigidity of a graph
# import relevant modules
import random
import numpy as np

####################################################################################################
# create a function that plots the graph on the x-y plane
def G_configuration(G):
    
    # set the seed for reproducibility
    #random.seed(132)
    
    num_of_nodes = len(G.nodes)
    x_nodes = []
    y_nodes = []
    
    # create random coordinates for each node in the graph
    # use a lot of integers for randomised, like 2e40
    for i in range(num_of_nodes):
        x = random.randint(-2 * 10 ** 40, 2 * 10 ** 40)
        y = random.randint(-2 * 10 ** 40, 2 * 10 ** 40)
        x_nodes.append(x)
        y_nodes.append(y)
        
    return x_nodes, y_nodes

####################################################################################################
# create the rigidity matrix

# create a matrix that is n row and d*n columns
# only consider d = 2 for now
def rigidity_matrix(G):
    
    # extract the coordinates of the graph
    x_nodes, y_nodes = G_configuration(G)
    
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
    
    # find the rigidity matrix of G
    R = rigidity_matrix(G)
    
    # find the rank of R
    R_rank = np.linalg.matrix_rank(R)
    
    # check whether the rank satsifies Infinitesimal rigidity condition
    if R_rank == 2*n - 3:
        return True
    else:
        return False
    
####################################################################################################

# find rigid graphs given planar graphs satisfying 2n - 3 edges
# we don't consider the graphs that have vertices with degree 2
# let v be the number of vertices, and Graphs be the list of graphs
def find_rigid_graphs(Graphs):
    
    # all graphs have the same number of vertices
    # we consider any one of these graphs and count how many there are    
    n = len(Graphs[0].nodes())
    
    # filter out the graphs that have degree 2 vertices
    graphs_without_degree_2 = []
    
    for i in range(len(Graphs)):
        
        G = Graphs[i]
        has_low_degree = False
        
        for j in range(n):
            if len(list(G[j])) <= 2:
                has_low_degree = True
                break
            
        if has_low_degree == False:
            graphs_without_degree_2.append(G)
    
    # identify rigid graphs
    rigid_graphs = []
    
    for i in range(len(graphs_without_degree_2)):
        G = graphs_without_degree_2[i]
        
        if check_rigidity(G) == True:
            rigid_graphs.append(G)
    
    return rigid_graphs

####################################################################################################


