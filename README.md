# Minimally Rigid Graphs and their Circle Packings

This repository contains the Python code involved in my final year dissertation project for the academic year 2023/2024. I was supervised by Dr Louis Theran, and investigated the the existence of circle packings for a given minimally rigid graph using numerical optimization methods.

I was awarded a First Class Honors grade for the project, and it's up here for people to view and play with if interested :)

![image](https://github.com/user-attachments/assets/d542dc06-cdc1-4a1d-bcbf-875b37516e33)


## The code involved

- `Rigidity.py` contains functions that computes the rigidity matrix of a given graph/framework and verifies whether it is infinitesimally rigid
- `Circle_Packing.py` takes a graph `G` and tries to find a circle packing for the graph. This is done using the `scipy.minimize` function, using the `COBYLA` method as it works well with problems that have constraints to adhere to. 
- Finally, `Rigid_Packings.py` finds all minimally rigid graphs on $n$ vertices, and attempts to find a circle packing for each of these graphs such that the contact graph of the circle packing is infinitesimally rigid itself. 

## The Algorithm

The algorithm used to investigate the graphs of interest is noted in Write-up/Dissertation.pdf on page 45 under 'Algorithm 4.2', but it is mentioned here as well for completeness.

![image](https://github.com/user-attachments/assets/8eb3446e-efe2-4e0d-8518-ba78c3e0abea)
