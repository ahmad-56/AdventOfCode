from input import user_input

splited = list(user_input)
current_floor = 0

for i in splited:
    if i == '(':
        current_floor += 1
    elif i == ')':
        current_floor -= 1

print(current_floor)