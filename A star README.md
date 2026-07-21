function AStar(start, goal):
open_list ← [start]
closed_set ← ∅

while open_list not empty:
current ← node with lowest f = g + h

if current = goal:
return path from start to goal

move current from open_list to closed_set

for each neighbor of current:
if neighbor is obstacle or in closed_set:
continue

g ← current.g + cost
h ← heuristic(neighbor, goal)
f ← g + h

if neighbor not in open_list OR f < neighbor.f:
update neighbor (g, h, f, parent)
add neighbor to open_list

return failure
