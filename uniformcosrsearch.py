import heapq

class Node:
    def __init__(self, state, cost):
        self.state = state
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def uniform_cost_search(start, goal, graph):
    priority_queue = []
    heapq.heappush(priority_queue, Node(start, 0))
    explored = set()
    costs = {start: 0}

    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        current_state = current_node.state

        if current_node.cost > costs[current_state]:
            continue

        if current_state == goal:
            return costs[current_state]

        explored.add(current_state)

        for neighbor, cost in graph.get(current_state, {}).items():
            if neighbor not in explored:
                new_cost = costs[current_state] + cost
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    heapq.heappush(priority_queue, Node(neighbor, new_cost))

    return float('inf')  # Return infinity if the goal is not reachable

# Example graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'E': 1},
    'D': {'B': 2, 'E': 3},
    'E': {'B': 5, 'C': 1, 'D': 3}
}

# Running the UCS
cost = uniform_cost_search('A', 'E', graph)
print(f"Cost from A to E: {cost}")
