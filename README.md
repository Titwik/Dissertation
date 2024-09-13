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

### Algorithm 4.2

1) Generate a list of planar graphs on n vertices and $2n − 3$ edges using `nauty`.
2) Use find rigid graphs from `Rigidity.py` and filter the list for minimally rigid planar graphs on $n$ vertices and minimum degree 3. Call this list `rigid graphs`.
3) Initialize variables `attempt = 0`,` position = 0` and `max attempt = 500`.
4) While `True`:
	5) Increment `attempt` by 1.
	6) Call `circle packing` from `Circle Packing.py` for `rigid graphs[position]`.
	7) If the contact graph of the packing is isomorphic to `rigid graphs[position]` **and**
		`check rigidity(contact graph)` returns `True` **and** `position` is less than the length of `rigid graphs`:
		8) Save `G`, `contact graph` `fig1`, `fig2` and `fig3`.
		9) Increment `position` by 1.
		10) Set `attempt` to 0.
	11) Else if the contact graph of the packing is isomorphic to `rigid graphs[position]` **and** `check rigidity(contact graph)` returns `True` **and** `position` is equal to the length of `rigid graphs`:
		12) Save `G`, `contact graph` `fig1`, `fig2` and `fig3`.
		13) `break` out of the loop
	14) Else if the contact graph of the packing is not isomorphic to `rigid graphs[position]`, **or** `check rigidity(contact graph)` returns `False`, **and** `attempt` is equal to `max attempt`:
		15) print “Max attempts done, no viable packing found. Code terminating”
		16) `break` out of the loop
