from collections import deque

# Sample graph represented as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
}

# BFS Implementation
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph.get(node, []))

# DFS Implementation (recursive)
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs_recursive(graph, neighbor, visited)


            

# Example usage
print("BFS starting from A:")
bfs(graph, 'A')

print("\nDFS (recursive) starting from A:")
dfs_recursive(graph, 'A')

