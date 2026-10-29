import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H'],
    'E': ['B', 'H'],
    'F': ['C', 'H'],
    'G': ['C', 'H'],
    'H': ['D', 'E', 'F', 'G']
}

h = {'A': 6, 'B': 4, 'C': 3, 'D': 2, 'E': 3, 'F': 2, 'G': 1, 'H': 0}

def greedy(start, goal):
    pq = [(h[start], start, [start])]
    visited = set()

    while pq:
        _, node, path = heapq.heappop(pq)

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    heapq.heappush(pq, (h[n], n, path + [n]))

    return None

print("Path:", greedy('A', 'H'))
