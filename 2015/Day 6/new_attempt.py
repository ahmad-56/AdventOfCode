def grid():
    array = [[0 for i in range(1000)] for j in range(1000)]
    return array

def coordinates(operation):
    if operation == "turn":
        operation = words[1]
        coord1 = words[2]
        p1 = coord1.split(",")
        x1 = int(p1[0])
        y1 = int(p1[-1])
        coord2 = words[-1]
        p2 = coord2.split(",")
        x2 = int(p2[0])
        y2 = int(p2[-1])
    else:
        coord1 = words[1]
        p1 = coord1.split(",")
        x1 = int(p1[0])
        y1 = int(p1[-1])
        coord2 = words[-1]
        p2 = coord2.split(",")
        x2 = int(p2[0])
        y2 = int(p2[-1])
    return x1,y1,x2,y2,operation
 
from input import user_input

grid_box = grid()
lines = user_input.splitlines()
for line in lines:
    # find what you need to do to the lights
    words = line.split()
    operation = words[0]

    x1,y1,x2,y2,operation = coordinates(operation) #update upto scenario

    if operation == "on": 
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                grid_box[i][j] = 1
    elif operation == "off": 
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                grid_box[i][j] = 0
    elif operation == "toggle": 
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if grid_box[i][j] == 1:
                    grid_box[i][j] = 0
                else:
                    grid_box[i][j] = 1

ans = sum(row.count(1) for row in grid_box)
print(ans)