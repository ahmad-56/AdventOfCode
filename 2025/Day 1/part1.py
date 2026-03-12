from input import user_input

array = []
for i in range(-1,99):
    array.append(i+1)
count = 0
position = 50
pos = 0
lines = user_input.splitlines()
for line in lines: 
    condition = line[0]
    movement_array=[]
    movement = ""
    
    for i in line:
        if i.isnumeric():
            movement_array.append(i)
    for i in movement_array: 
        movement += str(i)

    if condition == "R":
        pos = position + int(movement)
        if pos > 99 and pos < 999:
            no_ = str(pos)[0]
            if no_ == "-":
                no_ = str(pos)[1]    
            no_ = int(no_) * 100
            pos -= no_
        elif pos > 999:
            no_ = str(pos)[0]
            if no_ == "-":
                no_ = str(pos)[1] + str(pos)[2]
            else:
                no_ = str(pos)[0] + str(pos)[1]
            no_ = int(no_) * 100
            pos -= no_
        position = array[pos]
    elif condition == "L":
        pos = position - int(movement)
        if pos < -99 and pos > -999:
            no_ = str(pos)[0]
            if no_ == "-":
                no_ = str(pos)[1]    
            no_ = int(no_) * 100
            pos += no_
        elif pos < -999:
            no_ = str(pos)[0]
            if no_ == "-":
                no_ = str(pos)[1] + str(pos)[2]
            else:
                no_ = str(pos)[0] + str(pos)[1]
            no_ = int(no_) * 100
            pos -= no_
        position = array[pos]
    if  position == 0:
        count += 1

print(f"Password: {count}")