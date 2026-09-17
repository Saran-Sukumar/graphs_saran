# graphs_saran

This project implements Dijkstra's shortest path algorithm packaged as a Python library.  
It is part of CS 3250 Homework 5, where the goal is to learn how to package Python code into a standardized, installable format.



## Package Name

The package name follows the required format:

graphs_<unique_id>

For this project:

graphs_saran



## Repository Structure

src/
    graphs_saran/
        __init__.py
        heapq.py
        sp.py
test.py
README.md
pyproject.toml



## Installation

Install the package using pip:

pip install .

Or install directly from GitHub:

pip install git+https://github.com/Saran-Sukumaran/graphs_saran.git



## Usage Example

Replace `graphs_saran` with your own unique ID if needed:

```python
from graphs_saran import sp
import sys

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print(f'Use: {sys.argv[0]} graph_file')
        sys.exit(1)

    graph = {}
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            line = line.strip()
            s, d, w = line.split()
            s = int(s)
            d = int(d)
            w = int(w)
            if s not in graph:
                graph[s] = {}
            graph[s][d] = w
    
    s = 0
    dist, path = sp.dijkstra(graph, s)
    print(f'Shortest distances from {s}:')
    print(dist)
    for d in path: 
        print(f'spf to {d}: {path[d]}")
