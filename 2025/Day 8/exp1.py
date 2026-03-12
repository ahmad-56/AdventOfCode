from BubbleSort import bubble_sort
user_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

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

sorted_dist, sorted_index = bubble_sort(dist_array, index_array)

#print(sorted_dist)
print(sorted_index)

#shortest = min(dist_array)
#index_shortest = index_array[dist_array.index(shortest)]
#print(index_shortest)