# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 19:52:29 2023

@author: Titwik
"""

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
# Examples of planar and minimally rigid
# Minimally rigid graphs have 2n-3 edges, where n is number of nodes

Graphs = []

#1
G1 = nx.Graph()
G1.add_edge(0, 1)
G1.add_edge(2, 1)
G1.add_edge(2, 0)
Graphs.append(G1)
#plt.title('G1')
#nx.draw_planar(G1,with_labels = True)

#2
G2 = nx.Graph()
G2.add_edge(0, 1)
G2.add_edge(2, 1)
G2.add_edge(2, 0)
G2.add_edge(2,3)
G2.add_edge(3,0)
Graphs.append(G2)
#plt.title('G2')
#nx.draw_planar(G2,with_labels = True)

#3 
G3 = nx.Graph()
G3.add_edge(0,1)
G3.add_edge(2,1)
G3.add_edge(2,3)
G3.add_edge(4,3)
G3.add_edge(0,4)
G3.add_edge(1,4)
G3.add_edge(2,4)
Graphs.append(G3)
#plt.title('G3')
#nx.draw_planar(G3,with_labels = True)

#4
G4 = nx.Graph()
G4.add_edge(0,1)
G4.add_edge(2,1)
G4.add_edge(2,3)
G4.add_edge(0,3)
G4.add_edge(0,4)
G4.add_edge(1,4)
G4.add_edge(3,4)
Graphs.append(G4)
#plt.title('G4')
#nx.draw_planar(G4,with_labels = True)

#5
G5 = nx.Graph()
G5.add_edge(0,1)
G5.add_edge(0,3)
G5.add_edge(2,1)
G5.add_edge(1,4)
G5.add_edge(2,4)
G5.add_edge(1,3)
G5.add_edge(3,4)
G5.add_edge(5,4)
G5.add_edge(3,5)
Graphs.append(G5)
#plt.title('G5')
#nx.draw_planar(G5,with_labels = True)

#6
G6 = nx.Graph()
G6.add_edge(0,1)
G6.add_edge(1,2)
G6.add_edge(2,3)
G6.add_edge(3,4)
G6.add_edge(5,4)
G6.add_edge(5,0)
G6.add_edge(2,0)
G6.add_edge(5,2)
G6.add_edge(3,5)
Graphs.append(G6)
#plt.title('G6')
#nx.draw_planar(G6,with_labels = True)


#7
G7 = nx.Graph()
G7.add_edge(0,1)
G7.add_edge(0,2)
G7.add_edge(0,3)
G7.add_edge(0,4)
G7.add_edge(0,5)
G7.add_edge(4,5)
G7.add_edge(3,4)
G7.add_edge(2,3)
G7.add_edge(1,2)
Graphs.append(G7)
#plt.title('G7')
#nx.draw_planar(G7,with_labels = True)

#8
G9 = nx.Graph()
G9.add_edge(0,1)
G9.add_edge(1,2)
G9.add_edge(2,3)
G9.add_edge(3,4)
G9.add_edge(0,4)
G9.add_edge(3,5)
G9.add_edge(5,1)
G9.add_edge(4,1)
G9.add_edge(4,5)
Graphs.append(G9)
#plt.title('G9')
#nx.draw_planar(G9,with_labels = True)

plt.show()

for i in range(len(Graphs)):
    fig = plt.figure()
    nx.draw_planar(Graphs[i],with_labels = True)
    plt.title(f'G{i+1}')
    plt.show()
    
# isomorphism checking code
def check_isomorphism(Graphs):
    for i in range(len(Graphs)):
        for j in range(len(Graphs)):    
            if nx.is_isomorphic(Graphs[i], Graphs[j]) == True and i != j:
                print(f'Graphs G{i+1} and G{j+1} are isomorphic')


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        