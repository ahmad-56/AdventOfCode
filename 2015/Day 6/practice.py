#grid_name[row_index][column_index] = new_value
import re

def grid():
    rows = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append(0)
        rows.append(row)
    return rows

grid_1 = grid()
input_1 = """(2,2)
(2,4)
(4,2)
(4,4)"""

input_1 = input_1.splitlines()
for line in input_1:
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
    
    
print(grid_1[3][3])