from gridfile import grid
import re

from input import user_input

grid_1 = grid()

splited = user_input.splitlines()
for line in splited:
    code_words = r"(toggle|turn off|turn on)"
    word = re.search(code_words, line).group(0)
    numbers = list(map(int, re.findall(r"\d+", line)))
    x1, y1, x2, y2 = numbers[0], numbers[1], numbers[-2], numbers[-1]

    if word == 'toggle':
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if grid_1[x][y] == 0:
                    grid_1[x][y] = 1
                else:
                    grid_1[x][y] = 0
    
    elif word == 'turn off':
        if grid_1[x][y] == 1:
            grid_1[x][y] = 0        
    elif word == 'turn on':
        if grid_1[x][y] == 0:
            grid_1[x][y] = 1        

total = 0
for row in grid_1:
    total += sum(row)

print("Total:", total)