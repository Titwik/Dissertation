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
        x = random.uniform(0,10)
        IC.append(x)
        
        y = random.uniform(0,10)
        IC.append(y)
        
        r = random.uniform(0,1)
        IC.append(r)
        
    return IC

###################################################################################################################

# code to find packings
def circle_packing(G):
    
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
        contacts = 0
        
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
                    contacts += 1
        
###################################################################################################################

        # code is successful if we get 2n-3 tangent circles
        if contacts == (2*n - 3):
            
            # generate the contact graph in networkx
            contact_graph = nx.Graph()
            
            # add an edge if two circles are tangential
            for i in range(n):
                x1, y1, r1 = x_list[i], y_list[i], r_list[i]

                for j in range(i+1, n):
                    x2, y2, r2 = x_list[j], y_list[j], r_list[j]
                    
                    if abs(np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) - (r1 + r2)) < tolerance:
                        contact_graph.add_edge(i, j)  # Add an edge between tangential circles
                
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

            # find the average of (x_min, x_max), (y_min, y_max)
            x_scale = (x_min+x_max)/2
            y_scale = (y_min+y_max)/2

            # create lists to store the centers after the packing is translated so that 
            # it is centered about the origin (0,0)
            x_center = []
            y_center = []

###################################################################################################################

            # generate a circle packing without the contact graph                               
            fig1, ax1 = plt.subplots()

            # draw the plots
            for i in range(n):
                    
                # identify the center and radius
                x, y, r = x_list[i], y_list[i], r_list[i]

                x_new, y_new = x-x_scale, y-y_scale
                x_center.append(x_new)
                y_center.append(y_new)
                    
                # Create the circle
                circle = plt.Circle((x_new, y_new), r, edgecolor='black', facecolor='none')

                # plot the center of the circle
                ax1.add_patch(circle)
            
###################################################################################################################            

            # generate the circle packing with its contact graph
            fig2, ax2 = plt.subplots()
                
            for i in range(n):
                    
                x = x_center[i]
                y = y_center[i]
                r = r_list[i]
                    
                # Create the circle
                circle = plt.Circle((x, y), r, edgecolor='black', facecolor='none')                  

                # plot the center of the circle
                plt.plot(x, y, marker='o', color='black') 
                ax2.add_patch(circle)

            # create the contact graph inside the circle packing
            for j in range(n):
                x1, y1, r1 = x_center[j], y_center[j], r_list[j]
                
                for k in range(j+1, n):
                    x2, y2, r2 = x_center[k], y_center[k], r_list[k]
                        
                    if abs(np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) - (r1 + r2)) < tolerance:
                        plt.plot([x1, x2], [y1, y2], color='black', linewidth = 0.5, linestyle = 'dashed') 

###################################################################################################################                            
                
            # ensure the plots are drawn on square axes
            # this ensures goof x_min < y_min:
                
            # hide the axes
            ax1.axis('off')
            ax2.axis('off')

            x_differences = [np.abs(x_center[i] - r_list[i]) for i in range(n)]
            y_differences = [np.abs(y_center[i] - r_list[i]) for i in range(n)]

            x_min = min(x_differences)
            x_max = max(x_differences)

            y_min = min(y_differences)
            y_max = max(y_differences)

            # Assuming you have computed x_min, x_max, y_min, and y_max after centering the circle packing
            # Compute the range value
            range_value = max(abs(x_min), abs(x_max), abs(y_min), abs(y_max))
                
            # display the plots
            fig1.set_figheight(8)
            fig1.set_figwidth(8)
            ax1.set(xlim=(-range_value,range_value), ylim=(-range_value, range_value))
            plt.xlabel('X-axis')  
            plt.ylabel('Y-axis')
                
            # display the plots
            fig2.set_figheight(8)
            fig2.set_figwidth(8)
            ax2.set(xlim=(-range_value,range_value), ylim=(-range_value, range_value))
            plt.xlabel('X-axis')  
            plt.ylabel('Y-axis')

            # return the contact graph separately
            plt.figure(figsize = (8,8))
            for i in range(n):
                    
                # identify the center and radius
                x, y, r = x_list[i], y_list[i], r_list[i]
                plt.plot(x, y, marker='o', color='black', markersize = 10) 
                    
                for j in range(n):
                    x1, y1, r1 = x_list[j], y_list[j], r_list[j]
                    
                    for k in range(j+1, n):
                        x2, y2, r2 = x_list[k], y_list[k], r_list[k]
                            
                        if abs(np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) - (r1 + r2)) < tolerance:
                            plt.plot([x1, x2], [y1, y2], color='black', linewidth = 0.5)                                

            plt.axis('off')
            fig3 = plt.gcf()
                
            # prevent the plots from displaying
            plt.close(fig1)
            plt.close(fig2)
            plt.close(fig3)
                
            return G, contact_graph, fig1, fig2, fig3

###########################################################################

