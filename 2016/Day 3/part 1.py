from input import user_input

triangles = 0
splited = user_input.splitlines()
for i in splited:
    lines = i.split()
    int_list = list(map(int, lines))

    for i in range(len(int_list)):
        num_1 = int_list[0]
        num_2 = int_list[1]
        num_3 = int_list[2]
        sum_of_sides_1 = num_1 + num_2
        sum_of_sides_2 = num_2 + num_3
        sum_of_sides_3 = num_1 + num_3

    if sum_of_sides_1 > num_3 and sum_of_sides_2 > num_1 and sum_of_sides_3 > num_2:
        triangles += 1

print(f"No. {triangles}")