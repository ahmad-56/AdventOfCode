#fewer than four rolls of paper in the eight adjacent positions
from input import user_input

linez = user_input.splitlines()
lines = []
for line in linez:    
    elements = list(line)
    elements.insert(0,"0")
    elements.append("0")
    lines.append(elements)
padding = list("0"*int(len(line)+2))
lines.append(padding)
lines.insert(0, padding)

Roll = 0

for i in range(1, len(line)+1):
    for j in range(1, len(line)+1):     
        check = 0
        place = lines[i][j]
        if place == "@":
            Right = lines[i][j+1]
            Left = lines[i][j-1]
            Up = lines[i-1][j]
            Down = lines[i+1][j]        
            R_Up = lines[i-1][j+1]
            R_Down = lines[i+1][j+1]
            L_Up = lines[i-1][j-1]
            L_Down = lines[i+1][j-1]

            array = [Right, Left, Up, Down, R_Up, R_Down, L_Up, L_Down]

            check = array.count("@")
            if check < 4:
                Roll += 1

print(f"Rolls: {Roll}")