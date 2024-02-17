import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt 
from scipy.optimize import minimize 

###################################################################################################################

# create a function to produce a pre-selected list of graphs with n vertices
# these are purely for testing. each graph chosen is known to be (minimally) rigid
def graph(n):

    if n == 3:
        return nx.complete_graph((3))

    # 4 vertices
    elif n == 4:
        edges = [(0,1), (1,2), (2,3), (3,0), (1,3)]
        G4 = nx.Graph()
        G4.add_edges_from(edges)
        return G4

    # 5 vertices
    elif n == 5:
        edges = [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 4)]
        G5 = nx.Graph()
        G5.add_edges_from(edges)
        return G5

    # 6 vertices
    elif n == 6:
        edges = [(0, 2), (0, 3), (0, 4), (1, 3), (1, 4), (1, 5), (2, 4), (2, 5), (3, 5)]
        G6 = nx.Graph()
        G6.add_edges_from(edges)
        return G6

    # 7 vertices
    elif n == 7:
        edges = [(0, 3), (0, 4), (0, 5), (1, 3), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 6), (4, 6)]
        G7 = nx.Graph()
        G7.add_edges_from(edges)
        return G7

    # 8 vertices
    elif n == 8:
        edges = [(0, 4), (0, 5), (0, 6), (1, 4), (1, 5), (1, 7), 
                (2, 4), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7), (4, 7)]
        G8 = nx.Graph()
        G8.add_edges_from(edges)
        return G8

    # 9 vertices
    elif n == 9:
        edges = [(0, 3), (0, 5), (0, 6), (1, 4), (1, 6), (1, 7), (2, 5), 
                 (2, 6), (2, 7), (2, 8), (3, 5), (3, 8), (4, 7), (4, 8), (6, 8)]
        G9 = nx.Graph()
        G9.add_edges_from(edges)
        return G9

    # 10 vertices
    elif n == 10:
        edges = [(0, 5), (0, 8), (0, 9), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), 
                (2, 9), (3, 6), (3, 8), (3, 9), (4, 7), (4, 8), (4, 9), (5, 8), (5, 9)]
        G10 = nx.Graph()
        G10.add_edges_from(edges)
        return G10

###################################################################################################################

# create the objective function
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

###################################################################################################################

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
            
        # radius at most 10
        constraints.append({'type': 'ineq', 'fun': lambda vars, i=i: 10 - vars[3*i + 2]}) 

        # constraint to prevent overlapping
        for j in range(len(G)):
            if i != j:
                constraints.append({'type': 'ineq', 'fun': lambda vars, i=i, j=j: # (xi - xj)^2 + (yi - yj)^2 >= (ri + rj)^2
                                    (vars[3*i] - vars[3*j])**2 + (vars[3*i + 1] - vars[3*j + 1])**2 - ((vars[3*i + 2]) + (vars[3*j + 2]))**2})           
        
    return constraints

###################################################################################################################

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

###################################################################################################################

# code to find packings
def circle_packing(G, graphs):
    
    # obtain the number of nodes in G
    n = len(G)

    # start finding a packing
    while True:
        
        # use the minimize function
        result = minimize(mk_obj(G), initial_conditions(G), constraints = cons(G), method='COBYLA')

        # create lists to store x, y and r
        x_list, y_list, r_list = [], [], []

        for i in range(n):
            x = result.x[3*i]
            x_list.append(x)

            y = result.x[3*i + 1]
            y_list.append(y)

            r = result.x[3*i + 2]
            r_list.append(r)

        # This counter counts how many circles are tangent to each other in the packing        
        # we expect 2n-3 tangential circles
        # Reset the counter for each iteration       
        counter = 0
        
        # set a tolerance for 0
        tolerance = 0.001

        # obtain the coordinates of the centers of two circles
        for i in range(n):
            x1 = x_list[i]
            y1 = y_list[i]
            for j in range(i+1,n):
                x2 = x_list[j]
                y2 = y_list[j]
                
                # check if the distance between the centers is equal to the sum of radii
                if abs(np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) - (r_list[i] + r_list[j])) < tolerance:
                    counter += 1
        
        # code is successful if we get 2n-3 tangent circles
        if counter == (2*n - 3):
            
            # generate the contact graph
            contact_graph = nx.Graph()
            
            # add an edge if two circles are tangential
            for i in range(n):
                x1, y1, r1 = x_list[i], y_list[i], r_list[i]

                for j in range(i+1, n):
                    x2, y2, r2 = x_list[j], y_list[j], r_list[j]
                    
                    if abs(np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) - (r1 + r2)) < tolerance:
                        contact_graph.add_edge(i, j)  # Add an edge between tangential circles
                
            # Check if the contact graph has vertices of degree 1 or 2
            bad_degree = any(contact_graph.degree(v) <= 2 for v in contact_graph.nodes())

            if (not bad_degree or len(G) <= 5) and graphs == True:
                
                # generate the circle packing
                fig, ax = plt.subplots()
                
                for i in range(n):
                    
                    # identify the center and radius
                    x, y, r = x_list[i], y_list[i], r_list[i]
                    
                    # Create the circle
                    circle = plt.Circle((x, y), r, edgecolor='black', facecolor='none')
                    ax.add_patch(circle)
                
                # draw the plots
                # find x_min, x_max, y_min and y_max
                x_min_values = []
                x_max_values = []
                y_min_values = []
                y_max_values = []
                
                for i in range(n):
                        
                    x_min_values.append(x_list[i] - r_list[i])
                    x_max_values.append(x_list[i] + r_list[i])
                    y_min_values.append(y_list[i] - r_list[i])
                    y_max_values.append(y_list[i] + r_list[i])
                        
                x_min = min(x_min_values)
                x_max = max(x_max_values)
                        
                y_min = min(y_min_values)
                y_max = max(y_max_values)
                
                # ensure the plots are drawn on square axes
                # this ensures good looking circles
                if x_min < y_min:
                    y_min = x_min
                else:
                    x_min = y_min
                    
                if x_max > y_max:
                    y_max = x_max
                else:
                    x_max = y_max
                
                # hide the axes
                ax.axis('off')
                
                # display the plots
                fig.set_figheight(8)
                fig.set_figwidth(8)
                ax.set(xlim=(x_min - 0.05,x_max + 0.05), ylim=(y_min - 0.05,y_max + 0.05))
                plt.xlabel('X-axis')  
                plt.ylabel('Y-axis')
                plt.title(f'Circle Packing for n = {n}')
                plt.show()

                nx.draw(G)
                plt.title(f'Associated Graph for n = {n}')
                plt.show()

                nx.draw_planar(contact_graph)
                plt.title(f'Contact Graph for n = {n}')
                plt.show()

                return G, contact_graph, fig, ax
    
            elif (not bad_degree or len(G) <= 5) and graphs == False: 
                
                # generate the circle packing
                fig, ax = plt.subplots()
                
                for i in range(n):
                    
                    # identify the center and radius
                    x, y, r = x_list[i], y_list[i], r_list[i]
                    
                    # Create the circle
                    circle = plt.Circle((x, y), r, edgecolor='black', facecolor='none')

                    # plot the center of the circle
                    plt.plot(x, y, marker='o', color='black', linestyle='None') 
                    ax.add_patch(circle)

                    # create the contact graph inside the circle packing
                    for i in range(n):
                        x1, y1, r1 = x_list[i], y_list[i], r_list[i]
                        for j in range(i+1, n):
                            x2, y2, r2 = x_list[j], y_list[j], r_list[j]
                            if abs(np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) - (r1 + r2)) < tolerance:
                                plt.plot([x1, x2], [y1, y2], color='blue')                                
                
                # draw the plots
                # find x_min, x_max, y_min and y_max
                x_min_values = []
                x_max_values = []
                y_min_values = []
                y_max_values = []
                
                for i in range(n):
                
                    x_min_values.append(x_list[i] - r_list[i])
                    x_max_values.append(x_list[i] + r_list[i])
                    y_min_values.append(y_list[i] - r_list[i])
                    y_max_values.append(y_list[i] + r_list[i])
                        
                x_min = min(x_min_values)
                x_max = max(x_max_values)
                        
                y_min = min(y_min_values)
                y_max = max(y_max_values)
                
                # ensure the plots are drawn on square axes
                # this ensures good looking circles
                if x_min < y_min:
                    y_min = x_min
                else:
                    x_min = y_min
                    
                if x_max > y_max:
                    y_max = x_max
                else:
                    x_max = y_max
                
                # hide the axes
                ax.axis('off')
                
                # display the plots
                fig.set_figheight(8)
                fig.set_figwidth(8)
                ax.set(xlim=(x_min - 0.05,x_max + 0.05), ylim=(y_min - 0.05,y_max + 0.05))
                plt.xlabel('X-axis')  
                plt.ylabel('Y-axis')
                plt.title(f'Circle Packing for n = {n}')
                plt.show()
                
                return G, contact_graph, fig, ax

###################################################################################################################
