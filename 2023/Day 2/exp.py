import re

user_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

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

        new_list = lines[2:]
    reds = []
    blues = []
    greens = []
        
    for i in range(0, len(new_list), 2):
        number = int(new_list[i])
        letter = new_list[i + 1]
        if letter == 'R':
            reds.append(number)
        elif letter == 'G':
            greens.append(number)
        elif letter == 'B':
            blues.append(number)

    for i in reds:
        val_1 = max(reds)
    for i in greens:
        val_2 = max(greens)
    for i in blues:
        val_3 = max(blues)

    final_val = val_1 * val_2 * val_3
    score += final_val

print(f"Score: {score}")
#score: 2286