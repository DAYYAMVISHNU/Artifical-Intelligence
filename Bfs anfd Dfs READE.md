BFS(graph, start):
    create empty set visited
    create queue with start node

    while queue is not empty:
        node = dequeue from queue
        if node not in visited:
            print node
            add node to visited
            enqueue all neighbors of node
DFS_Recursive(graph, node, visited):
    if visited is None:
        create empty set visited

    if node not in visited:
        print node
        add node to visited
        for each neighbor in graph[node]:
            DFS_Recursive(graph, neighbor, visited)
