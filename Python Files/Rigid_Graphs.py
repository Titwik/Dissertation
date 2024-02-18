import os
import Rigidity as rg
import networkx as nx
import Circle_Packing as cp
import matplotlib.pyplot as plt

# define a function to return a list of minimally rigid graphs on n vertices
def rigid_graphs(n):

    Graphs = nx.read_graph6(f"/home/titwik/Diss Work/Misc/Graphs/planar-{n}-{2*n-3}.g6")
    return rg.find_rigid_graphs(Graphs)

# define a function to check whether the starting rigid graph is isomorphic to the packing
def check_isomorphism(n):
    
    print(f'Number of nodes is {n}')

    # keep track of how many attempts it has been, and the graph we are investigating 
    attempt = 0     
    position = 0
    max_attempt = 500
    
    while True:
        
        attempt += 1
        if attempt == 1:    
            print(f'Begin checking for graph {position+1}')
            print(f'This is attempt {attempt}')
            
        else:
            print(f'This is attempt {attempt}.')
        
        # initialise the graphs we are analysing
        G, contact_graph, fig, fig2, fig3 = cp.circle_packing(rigid_graphs(n)[position], True)
        
        if not os.path.exists(f'/home/titwik/Diss Work/Misc/Packings/{n}/Graph {position+1}'):
            os.makedirs(f'/home/titwik/Diss Work/Misc/Packings/{n}/Graph {position+1}')
        
        # save the graph
        nx.draw(G, node_color='black', node_size=300, edge_color='black', linewidths=2)
        plt.savefig(f'/home/titwik/Diss Work/Misc/Packings/{n}/Graph {position+1}/1. Starting graph.png', dpi = 300)
        plt.close()
        
        nx.draw_planar(G, node_color='black', node_size=300, edge_color='black', linewidths=2)
        plt.savefig(f'/home/titwik/Diss Work/Misc/Packings/{n}/Graph {position+1}/2. Planar starting graph.png', dpi = 300)
        plt.close()
        
        # set conditions 
        # ADDED A CONDITION TO NOT CHECK GRAPH NUMBER 95 (POSITION 94)
        # GET RID OF IT
        if nx.is_isomorphic(G, contact_graph) == True and (position+1) < len(rigid_graphs(n)) and position != 94:
            print(f'An isomorphic packing exists for graph number {position+1}')
            print('')
            

            # save the figures           
            fig.savefig(f'/home/titwik/Diss Work/Misc/Packings/{n}/Graph {position+1}/3. Plain packing.png', dpi = 300)
            fig2.savefig(f'/home/titwik/Diss Work/Misc/Packings/{n}/Graph {position+1}/4. Packing with contact.png', dpi = 300)
            fig3.savefig(f'/home/titwik/Diss Work/Misc/Packings/{n}/Graph {position+1}/5. Contact.png', dpi = 300)

            # adjust the position and attempt number
            position += 1
            attempt = 0
        
        # ADDED A CONDITION TO NOT CHECK GRAPH NUMBER 95 (POSITION 94)
        # GET RID OF IT
        elif nx.is_isomorphic(G, contact_graph) == True and (position+1) == len(rigid_graphs(n)) and position != 94:
            print(f'An isomorphic packing exists for graph number {position+1}')
            print('')

            # save the figures
            fig.savefig(f'/home/titwik/Diss Work/Misc/Packings/{n}/Graph {position+1}/3. Plain packing.png', dpi = 300)
            fig2.savefig(f'/home/titwik/Diss Work/Misc/Packings/{n}/Graph {position+1}/4. Packing with contact.png', dpi = 300)
            fig3.savefig(f'/home/titwik/Diss Work/Misc/Packings/{n}/Graph {position+1}/5. Contact.png', dpi = 300)
            
            break
        
        elif nx.is_isomorphic(G, contact_graph) == False and attempt == max_attempt:
            print(f'{max_attempt} attempts done, no viable packing found. Code terminating')
            
            break
        

# testing
check_isomorphism(9)











