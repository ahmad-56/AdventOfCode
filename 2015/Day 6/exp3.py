#[[0,0,0,0,0,0]
# [0,0,0,0,0,0]]

import re
from gridfile import grid

user_input = """toggle 461,550 through 564,900
turn off 370,39 through 425,839
turn off 464,858 through 833,915"""

grid_1 = grid()

user_input = user_input.splitlines()
for line in user_input:
    numbers = list(map(int, re.findall(r"\d+", line)))
    x1, y1, x2, y2 = numbers[0], numbers[1], numbers[-2], numbers[-1]
    code_words = r"(toggle|turn off|turn on)"
    word = re.search(code_words, line)
    
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
    

    
print(grid_1[460][549])