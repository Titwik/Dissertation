import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt 
from scipy.optimize import minimize 

# 3 vertices
G3 = nx.complete_graph((3))

# 4 vertices
edges = [(0,1), (1,2), (2,3), (3,0), (1,3)]
G4 = nx.Graph()
G4.add_edges_from(edges)

# 5 vertices
edges = [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 4)]
G5 = nx.Graph()
G5.add_edges_from(edges)

# 6 vertices
edges = [(0, 2), (0, 3), (0, 4), (1, 3), (1, 4), (1, 5), (2, 4), (2, 5), (3, 5)]
G6 = nx.Graph()
G6.add_edges_from(edges)

####################################################################################################

# 8 vertices
edges = [(0, 4), (0, 5), (0, 6), (1, 4), (1, 5), (1, 7), 
         (2, 4), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7), (4, 7)]

# Create a graph
G8 = nx.Graph()

# Add nodes and edges to the graph
G8.add_edges_from(edges)

####################################################################################################

# 9 vertices
edges = [(0, 4), (0, 6), (0, 7), (1, 5), (1, 6), (1, 7), (2, 5), 
         (2, 6), (2, 8), (3, 5), (3, 7), (3, 8), (4, 7), (4, 8), (6, 8)]

# Create a graph
G9 = nx.Graph()

# Add nodes and edges to the graph
G9.add_edges_from(edges)

####################################################################################################

# 10 vertices
edges = [(0, 5), (0, 8), (0, 9), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), 
         (2, 9), (3, 6), (3, 8), (3, 9), (4, 7), (4, 8), (4, 9), (5, 8), (5, 9)]

# Create a graph
G10 = nx.Graph()

# Add nodes and edges to the graph
G10.add_edges_from(edges)

# set G
#G = G3
#G = G4
#G = G5
G = G6
#G = G8
#G = G9
#G = G10

def mk_obj(G):
    
    # create a function that gives the objective function of a graph
    def objective_function(vars):

        # format of the tuple 'vars' is (x1,y1,r1, x2,y2,r2, x3,y3,r3, ...)

        # create a function that returns all x-coordinates
        def x(i):
            return vars[3*i]
        
        # create a function that returns all y-coordinates
        def y(i):
            return vars[3*i + 1]
        
        # create a function that returns all radii
        def r(i):
            return vars[3*i + 2]
        
        # initialise a sum 
        total = 0

        # compute the objective function (xi - xj) ** 2 + (yi - yj) ** 2 - (ri + rj) ** 2
        for (i,j) in G.edges():
            total += ((x(i) - x(j)) ** 2 + (y(i) - y(j)) ** 2 - (r(i) + r(j)) ** 2) ** 2
        
        return total

    return objective_function

# specify the constraints
def cons(G):

    # set the constraints
    # radius should greater than 0
    # set an epsilon to ensure strictly positive solutions
    epsilon = 0.04
    constraints = []

    for i in range(len(G)):
            
        # radius greater than 0
        constraints.append({'type': 'ineq', 'fun': lambda vars, i=i: vars[3*i + 2] - epsilon}) 
            
        # radius at most 1
        constraints.append({'type': 'ineq', 'fun': lambda vars, i=i: 1 - vars[3*i + 2]}) 

        # constraint to prevent overlapping
        for j in range(len(G)):
            if i != j:
                constraints.append({'type': 'ineq', 'fun': lambda vars, i=i, j=j: # (xi - xj)^2 + (yi - yj)^2 >= (ri + rj)^2
                                    (vars[3*i] - vars[3*j])**2 + (vars[3*i + 1] - vars[3*j + 1])**2 - ((vars[3*i + 2]) + (vars[3*j + 2]))**2})           
        
    return constraints
    

# set an initial guess
def initial_conditions(G):
    
    # find the number of nodes of G
    n = len(G)
    
    # create a list to store initial conditions
    IC = []
    
    # generate random numbers for x,y and r
    for i in range(n):
        x = random.uniform(0,6)
        IC.append(x)
        
        y = random.uniform(0,6)
        IC.append(y)
        
        r = random.uniform(0,1)
        IC.append(r)
        
    return IC

# set the constraints for G
constraints = cons(G)

# ensure that we get a packing that has a contact graph of 2n-3 edges
n = len(G)
while True:
    
    # use the minimize function
    result = minimize(mk_obj(G), initial_conditions(G), constraints = constraints, method='COBYLA')

    # create lists to store x, y and r
    x_list, y_list, r_list = [], [], []

    for i in range(n):
        x = result.x[3*i]
        x_list.append(x)

        y = result.x[3*i + 1]
        y_list.append(y)

        r = result.x[3*i + 2]
        r_list.append(r)

    # Reset the counter for each iteration
    # this counter counts how many circles are tangent to each other in the packing
    # we expect 2n-3 tangential circles
    counter = 0

    for i in range(n):
        x1 = x_list[i]
        y1 = y_list[i]
        for j in range(i+1,n):
            x2 = x_list[j]
            y2 = y_list[j]
            if np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) - (r_list[i] + r_list[j]) < 0.001:
                counter += 1
    
    if counter == (2 * n - 3):
        
        # generate a circle packing
        fig, ax = plt.subplots()
        
        print("Optimal solution:")
        for i in range(len(G)):
            print(f'x{i+1}, y{i+1}, r{i+1}: {result.x[3*i], result.x[3*i+1], result.x[3*i+2]}')
            
            x = result.x[3*i]
            x_list.append(x)

            y = result.x[3*i + 1]
            y_list.append(y)

            r = result.x[3*i + 2]
            r_list.append(r)
            
            # Create the circle
            circle = plt.Circle((x, y), r, edgecolor='black', facecolor='none')  # You can customize edgecolor and facecolor
            ax.add_patch(circle)
        
        # break out of the while loop
        break

fig.set_figheight(8)
fig.set_figwidth(8)
ax.set(xlim=(min(x_list) - 0.5, max(x_list) + 0.5), ylim=(min(y_list) - 0.5, max(y_list) + 0.5))
plt.xlabel('X-axis')  
plt.ylabel('Y-axis')
plt.title('Circle Packing')
plt.show()


















