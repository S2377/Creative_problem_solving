from collections import deque
def validPath(n, edges, source, destination):
    # graph as adjacency list
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    queue = deque([source])
    visited = set([source])
    while queue:
        current = queue.popleft()
        if current == destination:
            return True
        # Traverse neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

def validPath(n, edges, source, destination):
    # graph as adjacency list
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    stack = [source]
    visited = set([source])
    while stack:
        node = stack.pop()
        if node == destination:
            return True
        # Traverse neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    # If no path found
    return False    

