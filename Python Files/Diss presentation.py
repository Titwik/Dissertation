import Rigidity as rg
import Circle_Packing as cp
import networkx as nx
import matplotlib.pyplot as plt

# create different graphs to test
# inf rigid examples
G1 = nx.Graph()
G1.add_edges_from([(0,1), (1,2), (2,0)])
plt.title('Triangle')
nx.draw_planar(G1)
plt.show()
cp.circle_packing(G1)
plt.show()

print('Is the triangle is rigid')
print(rg.check_rigidity(G1))
print('')

G2 = nx.Graph()
G2.add_edges_from([(0,1), (1,2), (2,3), (3,0), (0,2)])
plt.title('Two-triangle')
nx.draw_kamada_kawai(G2)
plt.show()
cp.circle_packing(G2)
plt.show()

print('Is the two-triangle graph is rigid')
print(rg.check_rigidity(G2))
print('')

# inf flexible examples
G3 = nx.Graph() 
G3.add_edges_from([(0,1), (1,2), (2,3), (3,0)])
plt.title('Square')
nx.draw_kamada_kawai(G3)
plt.show()
print('Is the square is rigid')
print(rg.check_rigidity(G3))
print('')

# a complicated example
def rigid_graphs(n):

    Graphs = nx.read_graph6(f"/home/titwik/Diss Work/Misc/Graphs/planar-{n}-{2*n-3}.g6")
    return rg.find_rigid_graphs(Graphs)


Graph = rigid_graphs(7)[1]
nx.draw_planar(Graph)
plt.title('Harder Graph')
plt.show()
print('Is the harder graph rigid?')
print(rg.check_rigidity(Graph)) 
print('')

while True:
    
    G, contact_graph, fig1, fig2, fig3 = cp.circle_packing(Graph)
    if nx.is_isomorphic(G, contact_graph) == True and rg.check_rigidity(contact_graph) == True:
        
        print('A winning circle packing is found!')
    
        break
    else:
        print('Keep waiting...')
        
        
        
  




















