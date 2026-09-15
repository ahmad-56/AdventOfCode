from pathlib import Path
from itertools import permutations

input_file = Path(r"C:\Users\snoor\OneDrive\Desktop\Python\AdventofCode\2015\Day 9\sample_input.txt")

with input_file.open("r") as file:
    user_input = file.readlines()

locations = []
array = []
lines = user_input
for line in lines:
    line = line.split()
    loc1 = line[0]
    loc2 = line[2]
    if loc1 not in locations:
        locations.append(loc1)
    if loc2 not in locations:
        locations.append(loc2)
    dist = line[-1]

    array.append([loc1,loc2,dist])

routes = permutations(locations)

total = [] 
for route in routes:
    distance = 0
    for i in range(len(route) - 1):
        location = route[i]
        next = route[i + 1]

        for s in array:
            if location in s and next in s:
                distance += int(s[-1])
                break
    total.append(distance)

print(f"Minimum Distance: {min(total)}")