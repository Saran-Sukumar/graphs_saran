import sys
import heapq

def dijkstra(graph, source):
    dist = {v: sys.maxsize for v in graph}
    dist[source] = 0

    path = {}
    heap = [(0, source)]

    while heap:
        current_dist, u = heapq.heappop(heap)

        if current_dist > dist[u]:
            continue

        for v in graph[u]:
            weight = graph[u][v]
            new_dist = current_dist + weight

            if new_dist < dist[v]:
                dist[v] = new_dist
                path[v] = u
                heapq.heappush(heap, (new_dist, v))

    return dist, path
