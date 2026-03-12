from input import user_input
import re

#with only 12 red cubes, 13 green cubes, and 14 blue cubes.
#find sum of IDs
colours = {
    "blue":"B",
    "red":"R",
    "green":"G"
}

score = 0

for k,v in colours.items():
    user_input = user_input.replace(k,v) 

splited = user_input.splitlines()
for i in splited:
    lines = re.split(r'[,:; ]', i)
    for i in lines:
        if i == '':
            lines.remove(i)

        game_id = int(lines[1])
        new_list = lines[2:]

    for i in range(0, len(new_list), 2):
        valid = True
        number = int(new_list[i])
        letter = new_list[i + 1]
        
        if letter == 'R' and number > 12:
            valid = False
            break
        elif letter == 'G' and number > 13:
            valid = False
            break
        elif letter == 'B' and number > 14:
            valid = False
            break

    if valid:
        score += game_id

print(f"Score: {score}")

