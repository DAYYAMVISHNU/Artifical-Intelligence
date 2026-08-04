# Map Colouring Algorithm (Pseudo Code)

## Problem
Assign colours to regions of a map such that:
- No two adjacent regions share the same colour.
- Use a limited set of colours.

---

## Pseudo Code

FUNCTION is_valid(region, color):
    FOR each neighbor IN adjacency_list[region]:
        IF neighbor has assigned color == color:
            RETURN False
    RETURN True

FUNCTION color_map(region_list, index):
    IF index == length(region_list):
        RETURN True   // All regions coloured successfully

    region = region_list[index]

    FOR each color IN available_colors:
        IF is_valid(region, color):
            assign color to region
            IF color_map(region_list, index + 1):
                RETURN True
            remove assigned color (backtrack)

    RETURN False   // No valid colouring found

---

## Steps
1. Represent the map as a graph (regions + adjacency list).
2. Define a set of available colours.
3. Start colouring regions one by one using recursion.
4. At each step:
   - Check if the chosen colour is valid (no neighbour conflict).
   - If valid, assign and move to the next region.
   - If invalid, try another colour.
   - If no colour works, backtrack.
5. Continue until all regions are coloured or no solution exists.

---

## Example Output
