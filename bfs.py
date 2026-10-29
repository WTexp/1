graph = {
    'A': ['B', 'E', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'E', 'F', 'G'],
    'D': ['A', 'E'],
    'E': ['A', 'B', 'C', 'D', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['C', 'F']
}

queue = [['A']]
visited = ['A']

while queue:
    path = queue.pop(0)
    node = path[-1]

    if node == 'G':
        print("BFS Path:", ' -> '.join(path))
        break

    for n in graph[node]:
        if n not in visited:
            visited.append(n)
            queue.append(path + [n])
