import numpy as np
import networkx as nx
import matplotlib.pyplot as plt 
from scipy.optimize import minimize

# example G for testing purposes
# 8 vertices

nodes = [0, 1, 2, 3, 4, 5, 6, 7]
edges = [(0, 4), (0, 5), (0, 6), (1, 4), (1, 5), (1, 7), 
         (2, 4), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7), (4, 7)]

# Create a graph
G8 = nx.Graph()

# Add nodes and edges to the graph
G8.add_nodes_from(nodes)
G8.add_edges_from(edges)

####################################################################################################

# 9 vertices
nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
edges = [(0, 4), (0, 7), (0, 8), (1, 5), (1, 6), (1, 8), 
         (2, 5), (2, 6), (2, 8), (3, 6), (3, 7), (3, 8), (4, 7), (4, 8), (5, 8)]

# Create a graph
G9 = nx.Graph()

# Add nodes and edges to the graph
G9.add_nodes_from(nodes)
G9.add_edges_from(edges)

####################################################################################################

# 10 vertices
nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
edges = [(0, 5), (0, 8), (0, 9), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), 
         (2, 9), (3, 6), (3, 8), (3, 9), (4, 7), (4, 8), (4, 9), (5, 8), (5, 9)]

# Create a graph
G10 = nx.Graph()

# Add nodes and edges to the graph
G10.add_nodes_from(nodes)
G10.add_edges_from(edges)

# set G
#G = G8
#G = G9
G = G10
####################################################################################################

# create a function that takes in a graph
def outer(G):

    # if G has 8 vertices, use a function designed to return the 
    # objective function for a graph on 8 vertices
    if len(nx.nodes(G)) == 8:

        def objective_function(vars):

            # initialise all the x's, y's and r's. The format I'm using is (x1,y1,r1,x2,y2,r2, ...)
            x1,y1,r1,x2,y2,r2,x3,y3,r3,x4,y4,r4,x5,y5,r5,x6,y6,r6,x7,y7,r7,x8,y8,r8 = vars

            # create a list to contain the x's, y's and r's
            x = [x1,x2,x3,x4,x5,x6,x7,x8]
            y = [y1,y2,y3,y4,y5,y6,y7,y8]
            r = [r1,r2,r3,r4,r5,r6,r7,r8]  

            # if an edge exists in graph G, compute the circle equation
            n = len(nx.nodes(G))

            edges = []
            for i in range(n):
                for j in range(n):
                    if (i,j) in G.edges() and (j,i) not in edges:
                        edges.append((i,j))                        
            
            # compute the RHS of the equations
            RHS = []
            for i in range(len(edges)):

                right_side = (((x[edges[i][0]] - x[edges[i][1]]) ** 2 +
                              (y[edges[i][0]] - y[edges[i][1]]) ** 2 -
                              (np.abs(r[edges[i][0]]) - np.abs(r[edges[i][1]]) ** 2))) ** 2
                
                RHS.append(right_side)
            
            # set the equations
            eq1 = RHS[0]
            eq2 = RHS[1]
            eq3 = RHS[2]
            eq4 = RHS[3]
            eq5 = RHS[4]
            eq6 = RHS[5]
            eq7 = RHS[6]
            eq8 = RHS[7]
            eq9 = RHS[8]
            eq10 = RHS[9]
            eq11 = RHS[10]
            eq12 = RHS[11]
            eq13 = RHS[12]

            equations = [eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8,eq9,eq10,eq11,eq12,eq13]
            
            return sum(equations)
        
        # return the objective function    
        return objective_function
    
    # if G has 9 vertices
    if len(nx.nodes(G)) == 9:

        def objective_function(vars):

            # identify all the x's, y's and r's. The format I'm using is (x1,y1,r1,x2,y2,r2, ...)
            x1,y1,r1,x2,y2,r2,x3,y3,r3,x4,y4,r4,x5,y5,r5,x6,y6,r6,x7,y7,r7,x8,y8,r8,x9,y9,r9 = vars

            # create a list to contain the x's, y's and r's
            x = [x1,x2,x3,x4,x5,x6,x7,x8,x9]
            y = [y1,y2,y3,y4,y5,y6,y7,y8,y9]
            r = [r1,r2,r3,r4,r5,r6,r7,r8,r9]  

            # if an edge exists in graph G, compute the circle equation
            n = len(nx.nodes(G))

            edges = []
            for i in range(n):
                for j in range(n):
                    if (i,j) in G.edges() and (j,i) not in edges:
                        edges.append((i,j))
            
            # compute the RHS of the equations
            RHS = []
            for i in range(len(edges)):

                right_side = (((x[edges[i][0]] - x[edges[i][1]]) ** 2 +
                              (y[edges[i][0]] - y[edges[i][1]]) ** 2 -
                              (np.abs(r[edges[i][0]]) - np.abs(r[edges[i][1]]) ** 2))) ** 2
                
                RHS.append(right_side)
            
            # set the equations
            eq1 = RHS[0]
            eq2 = RHS[1]
            eq3 = RHS[2]
            eq4 = RHS[3]
            eq5 = RHS[4]
            eq6 = RHS[5]
            eq7 = RHS[6]
            eq8 = RHS[7]
            eq9 = RHS[8]
            eq10 = RHS[9]
            eq11 = RHS[10]
            eq12 = RHS[11]
            eq13 = RHS[12]
            eq14 = RHS[13]
            eq15 = RHS[14]

            equations = [eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8,eq9,eq10,
                         eq11,eq12,eq13,eq14,eq15]
            
            return sum(equations)
        
        # return the objective function    
        return objective_function
    
    # if G has 10 vertices
    if len(nx.nodes(G)) == 10:

        def objective_function(vars):

            # identify all the x's, y's and r's. The format I'm using is (x1,y1,r1,x2,y2,r2, ...)
            x1,y1,r1,x2,y2,r2,x3,y3,r3,x4,y4,r4,x5,y5,r5,x6,y6,r6,x7,y7,r7,x8,y8,r8,x9,y9,r9,x10,y10,r10 = vars

            # create a list to contain the x's, y's and r's
            x = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
            y = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]
            r = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]  

            # if an edge exists in graph G, compute the circle equation
            n = len(nx.nodes(G))

            edges = []
            for i in range(n):
                for j in range(n):
                    if (i,j) in G.edges() and (j,i) not in edges:
                        edges.append((i,j))
            
            # compute the RHS of the equations
            RHS = []
            for i in range(len(edges)):

                right_side = (((x[edges[i][0]] - x[edges[i][1]]) ** 2 +
                              (y[edges[i][0]] - y[edges[i][1]]) ** 2 -
                              (np.abs(r[edges[i][0]]) - np.abs(r[edges[i][1]]) ** 2))) ** 2
                
                RHS.append(right_side)
            
            # set the equations
                
            eq1 = RHS[0]
            eq2 = RHS[1]
            eq3 = RHS[2]
            eq4 = RHS[3]
            eq5 = RHS[4]
            eq6 = RHS[5]
            eq7 = RHS[6]
            eq8 = RHS[7]
            eq9 = RHS[8]
            eq10 = RHS[9]
            eq11 = RHS[10]
            eq12 = RHS[11]
            eq13 = RHS[12]
            eq14 = RHS[13]
            eq15 = RHS[14]
            eq16 = RHS[15]
            eq17 = RHS[16]

            equations = [eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8,eq9,eq10,
                         eq11,eq12,eq13,eq14,eq15,eq16,eq17]
            
            return sum(equations)
        
        # return the objective function    
        return objective_function

# specify the constraints
def cons(G):

    # set the constraints
    # radius should greater than 0
    # set an epsilon to ensure strictly positive solutions
    epsilon = 1
    constraints = []

    for i in range(len(G)):
            
        # radius greater than 0
        constraints.append({'type': 'ineq', 'fun': lambda vars, i=i: vars[3*i + 2] - epsilon}) 
            
        # radius at most 1
        constraints.append({'type': 'ineq', 'fun': lambda vars, i=i: 1 - vars[3*i + 2]}) 

        # constraint to prevent overlapping
        for j in range(len(G)):
            if i != j:
                constraints.append({'type': 'ineq', 'fun': lambda vars, i=i, j=j: # (xi - xj)^2 + (yi - yj)^2 >= (ri - rj)^2
                                    (vars[3*i] - vars[3*j])**2 + (vars[3*i + 1] - vars[3*j + 1])**2 - (np.abs(vars[3*i + 2]) + np.abs(vars[3*j + 2]))**2})           
        
    return constraints
    

# set an initial guess
initial_guess_8 = [
    1.0, 1.0, 1.5,   # Circle 1: x1, y1, r1
    4.0, 1.0, 1.5,   # Circle 2: x2, y2, r2
    7.0, 1.0, 1.5,   # Circle 3: x3, y3, r3
    1.0, 4.0, 1.5,   # Circle 4: x4, y4, r4
    4.0, 4.0, 1.5,   # Circle 5: x5, y5, r5
    7.0, 4.0, 1.5,   # Circle 6: x6, y6, r6
    1.0, 7.0, 1.5,   # Circle 7: x7, y7, r7
    4.0, 7.0, 1.5    # Circle 8: x8, y8, r8
]

initial_guess_9 = [
    1.0, 1.0, 1.5,   # Circle 1: x1, y1, r1
    4.0, 1.0, 1.5,   # Circle 2: x2, y2, r2
    7.0, 1.0, 1.5,   # Circle 3: x3, y3, r3
    1.0, 4.0, 1.5,   # Circle 4: x4, y4, r4
    4.0, 4.0, 1.5,   # Circle 5: x5, y5, r5
    7.0, 4.0, 1.5,   # Circle 6: x6, y6, r6
    1.0, 7.0, 1.5,   # Circle 7: x7, y7, r7
    4.0, 7.0, 1.5,   # Circle 8: x8, y8, r8
    7.0, 7.0, 1.5    # Circle 9: x9, y9, r9
]


initial_guess_10 = [
    1.0, 1.0, 1.5,   # Circle 1: x1, y1, r1
    4.0, 1.0, 1.5,   # Circle 2: x2, y2, r2
    7.0, 1.0, 1.5,   # Circle 3: x3, y3, r3
    1.0, 4.0, 1.5,   # Circle 4: x4, y4, r4
    4.0, 4.0, 1.5,   # Circle 5: x5, y5, r5
    7.0, 4.0, 1.5,   # Circle 6: x6, y6, r6
    1.0, 7.0, 1.5,   # Circle 7: x7, y7, r7
    4.0, 7.0, 1.5,   # Circle 8: x8, y8, r8
    7.0, 7.0, 1.5,   # Circle 9: x9, y9, r9
    4.0, 10.0, 1.5   # Circle 10: x10, y10, r10
]

# set the constraints for G
constraints = cons(G)

# use the minimize function
if len(G.nodes()) == 8:
    result = minimize(outer(G), initial_guess_8, constraints = constraints, method='COBYLA')

elif len(G.nodes()) == 9:
    result = minimize(outer(G), initial_guess_9, constraints = constraints, method='COBYLA')

elif len(G.nodes()) == 10:
    result = minimize(outer(G), initial_guess_10, constraints = constraints, method='COBYLA')
    

print("Optimal solution:")

if len(G.nodes()) == 8:
    for i in range(len(G)):
        print(f'x{i+1}, y{i+1}, r{i+1}: {result.x[3*i], result.x[3*i+1], result.x[3*i+2]}')

if len(G.nodes()) == 9:
    for i in range(len(G)):
        print(f'x{i+1}, y{i+1}, r{i+1}: {result.x[3*i], result.x[3*i+1], result.x[3*i+2]}')

if len(G.nodes()) == 10:
    for i in range(len(G)):
        print(f'x{i+1}, y{i+1}, r{i+1}: {result.x[3*i], result.x[3*i+1], result.x[3*i+2]}')

####################################################################################################

# generate a circle packing
fig, ax = plt.subplots()

# create lists to store x, y and r
x_list, y_list, r_list = [], [], []

for i in range(len(G)):
    x = result.x[3*i]
    x_list.append(x)

    y = result.x[3*i + 1]
    y_list.append(y)

    r = result.x[3*i + 2]
    r_list.append(r)

    # Create the circle
    circle = plt.Circle((x, y), r, edgecolor='black', facecolor='none')  # You can customize edgecolor and facecolor
    ax.add_patch(circle)

fig.set_figheight(8)
fig.set_figwidth(8)
ax.set(xlim=(min(x_list) - 1.5, max(x_list) + 1.5), ylim=(min(y_list) - 1.5, max(y_list) + 1.5))
plt.xlabel('X-axis')  
plt.ylabel('Y-axis')
plt.title('Circle Packing')

plt.show()