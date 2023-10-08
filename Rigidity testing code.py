# Code to test the rigidity of a graph
# plan is to create a networkx graph and then, for each node, randomly assign 
# a point onto the x-y plane so that it can be analysed

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

plt.figure()
x = [1, 2, 3, 4, 5]
y = [2, 3, 1, 4, 5]

# Create a scatter plot
plt.scatter(x, y)

# Add labels and a title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of Points')

# Show the plot
plt.show()