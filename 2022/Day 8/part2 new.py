from file import input_file
filename = "puzzleinput.txt"
array = input_file(filename)

def count(place, position):
    counter = 0
    # for places RIGHT and DOWN
    if place == right or place == down:
        for num in place:
            counter += 1
            if num >= position:
                break
        return counter
    # for places LEFT and UP
    elif place == left or place == up:
        for num in reversed(place):
            counter += 1
            if num >= position:
                break
        return counter

scores = []
height = len(array)
length = len(array[0])
for i in range(height):
    for j in range(length):
        position = array[i][j]

        left = array[i][:j]
        right = array[i][j + 1:]
        up = [array[x][j] for x in range(0, i)]
        down = [array[x][j] for x in range(i + 1, height)]
        
        count_right = count(right, position)
        count_left = count(left, position)
        count_up = count(up, position)
        count_down = count(down, position)

        scenic_score = count_right * count_left * count_up * count_down
        scores.append(scenic_score)

print(f"Highest Scenic Score: {max(scores)}")