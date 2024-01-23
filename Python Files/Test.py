import numpy as np
import networkx as nx
from scipy.optimize import minimize
import matplotlib.pyplot as plt 

# example G for testing purposes
# 8 vertices

nodes = [0, 1, 2, 3, 4, 5, 6, 7]
edges = [(0, 4), (0, 5), (0, 6), (1, 4), (1, 5), (1, 7), 
         (2, 4), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7), (4, 7)]

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# create a function that takes in a graph
def outer(G):

    # if G has 8 vertices, use a function designed to return the 
    # objective function for a graph on 8 vertices
    if len(nx.nodes(G)) == 8:

        def objective_function(vars):

            # identify all the x's, y's and r's. The format I'm using is (x1,y1,r1,x2,y2,r2, ...)
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
                              (np.abs(r[edges[i][0]]) - np.abs(r[edges[i][1]])) ** 2)) ** 2
                
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
    
    # specify the constraints
def cons(G):
    # set the constraints
    # radius should be greater than 0
    # set an epsilon to ensure strictly positive solutions
    epsilon = 1
    constraints = []

    for i in range(8):
        constraints.append({'type': 'ineq', 'fun': lambda vars, i=i: vars[3*i + 2] - epsilon}) # radius greater than 0
        constraints.append({'type': 'ineq', 'fun': lambda vars, i=i: 1 - vars[3*i + 2]}) # radius at most 1

    # constraint to prevent overlapping
    for i in range(8):
        for j in range(8):
            if i != j:
                constraints.append({'type': 'ineq', 'fun': lambda vars, i=i, j=j: # (xi - xj)^2 + (yi - yj)^2 >= (ri - rj)^2
                                    (vars[3*i] - vars[3*j])**2 + (vars[3*i + 1] - vars[3*j + 1])**2 - (np.abs(vars[3*i + 2]) + np.abs(vars[3*j + 2]))**2})

    return constraints


# set an initial guess
initial_guess_8 = [
    1.5, 1.5, 1.0,   # Circle 1: x1, y1, r1
    4.0, 1.5, 1.0,   # Circle 2: x2, y2, r2
    7.0, 1.5, 1.0,   # Circle 3: x3, y3, r3
    1.5, 4.0, 1.0,   # Circle 4: x4, y4, r4
    4.0, 4.0, 1.0,   # Circle 5: x5, y5, r5
    7.0, 4.0, 1.0,   # Circle 6: x6, y6, r6
    1.5, 7.0, 1.0,   # Circle 7: x7, y7, r7
    4.0, 7.0, 1.0    # Circle 8: x8, y8, r8
]

# set the constraints for G
constraints = cons(G)

# use the minimize function
def circle_packing(G):
    if len(G.nodes()) == 8:
        result = minimize(outer(G), initial_guess_8, constraints = constraints, method='COBYLA')
    return result

print("Optimal solution:")

if len(G.nodes()) == 8:
    for i in range(8):
        print(f'x{i+1}, y{i+1}, r{i+1}: {circle_packing(G).x[3*i], circle_packing(G).x[3*i+1], circle_packing(G).x[3*i+2]}')

###########################################################################################################

# generate a circle packing
fig, ax = plt.subplots()

for i in range(len(G)):
    x = circle_packing(G).x[3*i]
    y = circle_packing(G).x[3*i + 1]
    r = circle_packing(G).x[3*i + 2]

    # Create the circle
    circle = plt.Circle((x, y), r, edgecolor='black', facecolor='none')  # You can customize edgecolor and facecolor
    ax.add_patch(circle)

fig.set_figheight(8)
fig.set_figwidth(8)
ax.set(xlim=(0, 7.2), ylim=(1, 8))
plt.xlabel('X-axis')  
plt.ylabel('Y-axis')
plt.title('Circle Packing')

plt.show()
                  











            


