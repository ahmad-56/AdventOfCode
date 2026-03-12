user_input="""London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

#London -> Dublin -> Belfast = 605

cities_1 = []
cities_2 = []
distances = []

total_distance = 0

splited = user_input.splitlines()
for i in splited:
    split = i.split()
    city_1 = split[0]
    city_2 = split[2]
    distance = split[-1]

    if city_1 not in cities_1:
        cities_1.append(city_1)
    if city_2 not in cities_2:
        cities_2.append(city_2)
    
print(cities_1)
print(cities_2)

for_shortest = []

for i in distances:
    total_distance += int(i)
    for_shortest.append(total_distance)

shortest_distance = 0

for i in range(len(for_shortest)-1):
    if for_shortest[i] < for_shortest[i+1]:
        shortest_distance = for_shortest[i]

print(f"Shortest Distance: {shortest_distance}")
#shortest route: 605