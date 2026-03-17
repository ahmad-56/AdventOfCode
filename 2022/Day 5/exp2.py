from file import input_file
import re
crate_order, user_input = input_file("exampleinput.txt")

# move 1 from 2 to 1
# move (number of crates) from (pick location) to (drop location)

array = []
count = 0
max = 0
lines = crate_order.splitlines()
for line in lines:
    ln = []
    for i in range(0, len(line), 4):
        newline = line[i:i+3]
        if max < len(newline):
            max = len(newline)
        if newline != "   ":
            count += 1
        ln.append(newline)        
    array.append(ln)

count -= len(array[-1])
length = len(array) - 1
for i in range(0, length):
    extras = ["   "] * max
    array.insert(0, extras)

for row in array:
    print(row)
print("----------------------")

for prompt in user_input:
    prompt = re.split(r"\s+", prompt)
    num = int(prompt[1]) # number of crates
    pick = int(prompt[3]) - 1 # pick location
    drop = int(prompt[-1]) - 1 # drop location
    i = 0
    if num == 1:
        for n in range(num):
            for i in range(len(array)):
                if array[i] != extras:
                    pos = array[i][pick]
                    if pos != "   ":
                        for j in range(1, len(array)):
                            new = array[-j][drop]    
                            if new == "   ":
                                array[-j][drop] = array[i][pick]
                                array[i][pick] = "   "
                                pos = ""
                                break
                    if pos == "":
                        break
    else:
        for n in range(num):
            for i in range(len(array)-2,-1,-1):
                if array[i] != extras:
                    pos = array[i][pick]
                    if pos != "   ":
                        for j in range(1, len(array)):
                            new = array[-j][drop]    
                            if new == "   ":
                                array[-j][drop] = array[i][pick]
                                array[i][pick] = "   "
                                pos = ""
                                break
                    if pos == "":
                        break
    for row in array:
        print(row)
    print("----------------------")

message = ""
for b in range(len(array[0])):
    for a in range(len(array)):
        place = array[a][b]
        if place != "   ":
            message += array[a][b][1]
            break
print(message) # MCD