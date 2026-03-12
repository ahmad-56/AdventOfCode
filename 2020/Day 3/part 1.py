from input import user_input

splitted = list(user_input)
house = 0

for i in splitted:
    if i == '>':
        if i == '<':
            break
        else: 
            house += 1
    elif i == '<':
        if i == '>':
            break
        else: 
            house += 1
    elif i == '^':
        if i == 'v':
            break
        else: 
            house += 1
    elif i == 'v':
        if i == '^':
            break
        else: 
            house += 1

print(house)