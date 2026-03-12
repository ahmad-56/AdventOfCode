user_input = """>^^v^<>"""

splitted = list(user_input)
house = 1
new = 0
position = []

for i in splitted:
    if i == '>':
        position.append('new')
        house += 1
        new += 1
    elif i == '<':
        position.append('W')
        house += 1
    elif i == '^':
        position.append('N')
        house += 1
    elif i == 'v':
        position.append('S')
        house += 1

print(house)
print(position)