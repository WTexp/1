
import heapq

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 3, 'E': 2},
    'C': {'A': 3, 'F': 2, 'G': 3},
    'D': {'B': 3, 'H': 3},
    'E': {'B': 2, 'H': 4},
    'F': {'C': 2, 'H': 3},
    'G': {'C': 3, 'H': 2},
    'H': {'D': 3, 'E': 4, 'F': 3, 'G': 2}
}

h = {'A': 5, 'B': 4, 'C': 3, 'D': 3,
     'E': 3, 'F': 2, 'G': 1, 'H': 0}

pq = [(h['A'], 0, 'A', ['A'])]
best = {'A': 0}

while pq:
    f, cost, node, path = heapq.heappop(pq)

    if node == 'H':
        print("Path:", path)
        print("Cost:", cost)
        break

    for n, w in graph[node].items():
        new_cost = cost + w

        if new_cost < best.get(n, float('inf')):
            best[n] = new_cost
            heapq.heappush(pq, (new_cost + h[n],
                                new_cost, n, path + [n]))
