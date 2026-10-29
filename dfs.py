graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

stack = [['A']]
visited = ['A']

while stack:
    path = stack.pop()
    node = path[-1]

    if node == 'G':
        print("DFS Path:", ' -> '.join(path))
        break

    for n in graph[node]:
        if n not in visited:
            visited.append(n)
            stack.append(path + [n])
