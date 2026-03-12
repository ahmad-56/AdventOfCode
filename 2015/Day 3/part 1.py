from input import user_input

splitted = list(user_input)
lists = []

while int(len(lists)) != 1001:
    listed = []
    for i in range(1,1001):
        listed.append(0)
    lists.append(listed)

x, y = 500, 500
lists[y][x] = 1 

for move in splitted:
    if move == '>':
        x += 1
    elif move == '<':
        x -= 1
    elif move == '^':
        y += 1
    elif move == 'v':
        y -= 1
    lists[x][y] += 1

answer = 0

for list in lists:
    for i in list:
        if i != 0:
            answer += 1
print(f"Houses which recieved atleast one present: {answer}")