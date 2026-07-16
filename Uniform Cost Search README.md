function UniformCostSearch(start, goal, graph):
    create priority_queue
    insert (start, cost=0) into priority_queue
    
    create explored_set
    create costs_map
    set costs[start] = 0
    
    while priority_queue is not empty:
        current_node = remove node with lowest cost from priority_queue
        current_state = current_node.state
        
        if current_node.cost > costs[current_state]:
            continue   // skip outdated entry
        
        if current_state == goal:
            return costs[current_state]   // found optimal path
        
        add current_state to explored_set
        
        for each neighbor in graph[current_state]:
            new_cost = costs[current_state] + edge_cost(current_state, neighbor)
            
            if neighbor not in explored_set:
                if neighbor not in costs_map OR new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    insert (neighbor, new_cost) into priority_queue
    
    return infinity   // goal not reachable
