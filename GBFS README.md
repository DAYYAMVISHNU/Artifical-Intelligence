function GreedyBestFirst(start, goal):
open_list ← [start] ordered by h
closed_set ← ∅

while open_list not empty:
current ← node with lowest h

if current = goal:
return path from start to goal

move current to closed_set

for each neighbor of current:
if neighbor is obstacle or in closed_set:
continue

h ← heuristic(neighbor, goal)

if neighbor not in open_list OR h < neighbor.h:
set neighbor.parent ← current
add neighbor to open_list

return failure
