from input import user_input

splitted = list(user_input)
santa_list = []
robo_santa_list = []

for i in range(0, len(splitted), 2):
    santa_list.append(splitted[i])

for i in range(1, len(splitted), 2):
    robo_santa_list.append(splitted[i])

lists = []

while int(len(lists)) != 1001:
    listed = []
    for i in range(1,1001):
        listed.append(0)
    lists.append(listed)

def moves(x,y):
    if move == '>':
        x += 1
    elif move == '<':
        x -= 1
    elif move == '^':
        y += 1
    elif move == 'v':
        y -= 1
    lists[x][y] += 1

    return

def starting_position():
    x, y = 500, 500
    lists[x][y] = 1 

starting_position()
for move in santa_list:
    moves()

starting_position()
for move in robo_santa_list:
    moves()

answer = 0

for list in lists:
    for i in list:
        if i != 0:
            answer += 1
print(f"Houses which recieved atleast one present: {answer}")

