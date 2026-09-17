from graphs_saran import sp

graph = {
    0: {1: 4, 7: 8},
    1: {2: 8},
    2: {3: 7, 5: 4, 8: 2},
    3: {},
    5: {},
    7: {},
    8: {}
}

dist, path = sp.dijkstra(graph, 0)
print("Distances:", dist)
print("Paths:", path)
