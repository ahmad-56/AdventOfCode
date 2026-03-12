user_input="""London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

#London -> Dublin -> Belfast = 605

dist_map = {}


cities_1 = []
cities_2 = []
distances = []

total_distance = 0

splited = user_input.splitlines()
for i in splited:
    split = i.split()
    city_1 = split[0]
    city_2 = split[2]
    distance = int(split[-1])

    dist_map[(city_1, city_2)] = distance
    dist_map[(city_2, city_1)] = distance

for key, value in distances.items():
    key[0]
print(dist_map)