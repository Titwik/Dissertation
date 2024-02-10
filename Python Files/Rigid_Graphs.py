import numpy as np
import Rigidity as rg
import networkx as nx
import Circle_Packing as cp
import matplotlib.pyplot as plt

# define a function to return a list of minimally rigid graphs on n vertices
def rigid_graphs(n):

    if n == 5:
        Graphs_5 = nx.read_graph6("/home/titwik/Diss Work/Misc/planar-5-7.g6")
        return rg.find_rigid_graphs(Graphs_5)

    elif n == 6:
        Graphs_6 = nx.read_graph6("/home/titwik/Diss Work/Misc/planar-6-9.g6")
        return rg.find_rigid_graphs(Graphs_6)

    elif n == 7:
        Graphs_7 = nx.read_graph6("/home/titwik/Diss Work/Misc/planar-7-11.g6")
        return rg.find_rigid_graphs(Graphs_7)

    elif n == 8:
        Graphs_8 = nx.read_graph6("/home/titwik/Diss Work/Misc/planar-8-13.g6")
        return rg.find_rigid_graphs(Graphs_8)

    elif n == 9:
        Graphs_9 = nx.read_graph6("/home/titwik/Diss Work/Misc/planar-9-15.g6")
        return rg.find_rigid_graphs(Graphs_9)
    
    elif n == 10:
        Graphs_10 = nx.read_graph6("/home/titwik/Diss Work/Misc/planar-10-17.g6")
        return rg.find_rigid_graphs(Graphs_10)

# define a function to check whether the starting rigid graph is isomorphic to the packing
def check_isomorphism(n):

    # keep track of how many attempts it has been, and the graph we are investigating 
    attempt = 0     
    position = 0   
    while True:
        
        attempt += 1
        if attempt == 1:    
            print(f'Begin checking for graph {position+1}')
            print(f'This is attempt {attempt}')
            
        else:
            print(f'This is attempt {attempt}.')
        
        G, contact_graph = cp.circle_packing(rigid_graphs(n)[position], drawing = False)
        
        if nx.is_isomorphic(G, contact_graph) == True and (position+1) < len(rigid_graphs(n)):
            print(f'An isomorphic packing exists for graph number {position+1}')
            print('')
            position += 1
            attempt = 0
        
        elif nx.is_isomorphic(G, contact_graph) == True and (position+1) == len(rigid_graphs(n)):
            print(f'An isomorphic packing exists for graph number {position+1}')
            print('')
            break
        
        elif attempt == 500:
            print('500 attempts done, no viable packing found. Code terminating')
            break
        

check_isomorphism(8)















