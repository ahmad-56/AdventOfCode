user_input = """30373
25512
65332
33549
35390"""

lines = user_input.splitlines()
height = len(lines)
array = []
scenic_score = []
visible = 0
for line in lines:
    length = len(line)
    columns = list(line)
    array.append(columns)
    edge = (height*2 + length*2) - 4
visible += edge

for i in range(1, height - 1):
    for j in range(1, length - 1):
        position = array[i][j]

        left = array[i][:j]
        right = array[i][j + 1:]
        up = [array[x][j] for x in range(0, i)]
        down = [array[x][j] for x in range(i + 1, height)]
        
        visible_left = len(left)
        visible_right = len(right)
        visible_up = len(up)
        visible_down = len(down)
        
        scenic_score_val = visible_right * visible_left * visible_up * visible_down
        scenic_score.append(scenic_score_val)

print(f"Best scenic score: {max(scenic_score)}")