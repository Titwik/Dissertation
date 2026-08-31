# Minimally Rigid Graphs and Their Circle Packings

This repository contains the Python implementation developed for my final year Mathematics dissertation at the University of St Andrews, supervised by Dr. Louis Theran. The dissertation investigated an open-ended question in rigidity theory, and was awarded a **First Class grade**. 

The project investigates the relationship between **minimal rigidity** and **circle packings**, with a particular focus on whether the contact graphs arising from circle packings of minimally rigid planar graphs retain infinitesimal rigidity.

The full dissertation is included in this repository as Write-Up/Dissertation.pdf for readers interested in the theoretical background, implementation details, and computational results.

## Example

| Minimally Rigid Graph | Circle Packing | Contact Graph |
|----------------------|----------------|---------------|
| A minimally rigid planar graph | Circle packing generated from the graph | Contact graph induced by circle tangencies |
| <img width="444" height="334" alt="image" src="https://github.com/user-attachments/assets/9e05bdfd-4013-403a-b5e7-a4153197cb0c" /> | <img width="421" height="392" alt="image" src="https://github.com/user-attachments/assets/a7a1b7c7-d9a7-4d8d-944a-973514c88c1f" /> | <img width="415" height="371" alt="image" src="https://github.com/user-attachments/assets/e683b089-15bf-41e2-a6ea-6d397ff529c0" /> |

---

# Background

A graph is **minimally rigid** if it is a Laman graph; that is, it has exactly 2|V| - 3 edges and every subgraph on $$k$$ vertices contains at most $$2k-3$$ edges. Equivalently, it is rigid on the minimum number of edges possible, so that removing any edge destroys rigidity.

A **circle packing** is a configuration of circles in $\mathbb{R}^2$ with disjoint interiors, where distinct circles may be tangent but never overlap. Associated with every packing is its **contact graph**, whose vertices correspond to circle centres, with an edge joining two vertices whenever the corresponding circles are tangent.

The central question investigated in this project is:

> For every planar and minimally rigid graph, does there exist a circle packing that is also infinitesimally rigid?

While the Circle Packing Theorem guarantees the existence of a circle packing whose contact graph is isomorphic to any planar graph, it is not known whether such a packing can always be chosen so that the resulting contact graph is infinitesimally rigid.

To explore this question computationally, algorithms were developed to:

1. Generate minimally rigid planar graphs.
2. Construct circle packings numerically.
3. Recover the contact graph of each packing.
4. Verify rigidity properties using rigidity matrices.

---

# Algorithm Overview

The computational search follows the procedure below:

```text
1. Generate all planar graphs on n vertices with 2n − 3 edges.
2. Filter the graphs to obtain minimally rigid planar graphs.
3. For each minimally rigid graph:

    a. Generate a circle packing.
    b. Construct the corresponding contact graph.
    c. Check whether the contact graph is isomorphic to the original graph.
    d. Verify infinitesimal rigidity of the contact graph.

4. Save graphs that satisfy both conditions:

       - Isomorphic contact graph
       - Infinitesimally rigid contact graph

5. Repeat until all candidate graphs have been examined.
```

For the complete version of the algorithm and theoretical justification, see:

**Write-up/Dissertation.pdf**, Algorithm 4.2.

---

# Modules

### `Rigidity.py`

Contains functions for:

- Generating generic graph configurations.
- Constructing rigidity matrices.
- Testing infinitesimal rigidity.
- Filtering collections of graphs for minimally rigid examples.

### `Circle_Packing.py`

Contains the constrained optimization routines used to:

- Construct circle packings for planar graphs.
- Determine circle centres and radii numerically.
- Enforce tangency and non-overlap constraints.
- Generate contact graphs.
- Visualize packings and their contact graphs.

The optimization is performed using the COBYLA algorithm from `scipy.optimize`.

### `Rigid_Packings.py`

Main driver script that:

- Retrieves minimally rigid planar graphs.
- Constructs circle packings.
- Generates contact graphs.
- Tests graph isomorphism.
- Verifies infinitesimal rigidity.
- Saves successful examples for further analysis.

---

## Results

Using the methods implemented in this repository, infinitesimally rigid circle packings were successfully constructed for all minimally rigid planar graphs on up to nine vertices.

For graphs on ten vertices, many valid examples were found, though computational limitations and the increasing number of local minima prevented an exhaustive search.

These results provide computational evidence supporting the conjecture for a large collection of minimally rigid planar graphs.

---

# About the Code

The code in this repository was written specifically for the computational experiments described in the dissertation. It is preserved here as a research artefact accompanying the project rather than as a polished software package.

While the code may be useful as a reference for readers interested in rigidity theory and circle packings, it was not designed for general use and may require additional datasets, generated graph files, or environment configuration not included in the repository.

---
