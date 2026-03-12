from input import user_input

line = list(user_input)
current_floor = 0
wanted_floor = -1
floors = 0
for i in line:
    if i == ")":
        current_floor -= 1
        floors += 1
        if current_floor == wanted_floor:
            break
    elif i == "(":
        current_floor += 1
        floors += 1
        if current_floor == wanted_floor:
            break

print(floors)