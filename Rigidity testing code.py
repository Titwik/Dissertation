# Code to test the rigidity of a graph
# plan is to create a networkx graph and then, for each node, randomly assign 
# a point onto the x-y plane so that it can be analysed
# use seed to ensure reproducibility 

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

plt.figure()
x = range(10)
y = range(3, 22, 2)

for i in range(9):
    line_x = [x[i], x[i + 1]]
    line_y = [y[i], y[i + 1]]
    plt.plot(line_x, line_y, 'k-')  

# Create a scatter plot
plt.plot(x, y, 'bo')
plt.plot(line_x, line_y, 'k-')

# Add labels and a title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()