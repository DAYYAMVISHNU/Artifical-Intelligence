# Map Colouring using Backtracking

# Example graph: each key is a region, values are its neighbours
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C']
}

# Available colours
colors = ['Red', 'Green', 'Blue']

# Dictionary to store assigned colours
assigned_colors = {}

def is_valid(region, color):
    """Check if assigning 'color' to 'region' is valid."""
    for neighbor in graph[region]:
        if neighbor in assigned_colors and assigned_colors[neighbor] == color:
            return False
    return True

def color_map(region_list, index=0):
    """Recursive backtracking to assign colours."""
    if index == len(region_list):
        return True  # All regions coloured successfully
    
    region = region_list[index]
    for color in colors:
        if is_valid(region, color):
            assigned_colors[region] = color
            if color_map(region_list, index + 1):
                return True
            # Backtrack
            assigned_colors.pop(region)
    return False

# Run colouring
regions = list(graph.keys())
if color_map(regions):
    print("Map colouring solution:")
    for region, color in assigned_colors.items():
        print(f"{region} → {color}")
else:
    print("No valid colouring found.")
