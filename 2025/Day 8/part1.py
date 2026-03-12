from input import user_input
from BubbleSort import bubble_sort

coords = []
lines = user_input.splitlines()
for line in lines:
    x, y, z = map(int, line.split(","))
    coords.append((x,y,z))
dist_array = []
index_array = []
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        x1, y1, z1 = coords[i]
        x2, y2, z2 = coords[j]
        dist = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2) ** 0.5
        dist_array.append(dist)
        index_array.append((i+1,j+1))

print(dist_array.sort())
shortest = min(dist_array)
index_shortest = index_array[dist_array.index(shortest)]

print(index_shortest)