from input import user_input
lines = user_input.splitlines()
height = len(lines)
array = []
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
        
        condition_left = all(position > num for num in left)
        condition_right = all(position > num for num in right)
        condition_up = all(position > num for num in up)
        condition_down = all(position > num for num in down)
        
        condition = condition_up or condition_down or condition_right or condition_left
        if condition:
            visible += 1

print(f"Total trees visible: {visible}")