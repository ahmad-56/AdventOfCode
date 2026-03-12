from input import user_input

splited = list(user_input)
current_floor = 0
wanted_floor = -1

for index, i in enumerate(splited):   
    if i == ')':
        current_floor -= 1
        if current_floor == wanted_floor:
            break
    elif i == '(':
        current_floor += 1
        if current_floor == wanted_floor:
            break
print(f"Position: {index + 1}")