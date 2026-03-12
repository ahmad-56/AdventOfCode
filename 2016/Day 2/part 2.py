#    1
#  2 3 4
#5 6 7 8 9
#  A B C
#    D
#U moves up, D moves down, L moves left, and R moves right

from input import user_input

keypad = []
code = []

for i in range(1, 10):
    keypad.append(i)
for i in range(65, 69):
    keypad.append(chr(i))

lines = user_input.splitlines()
position = 5 #int(keypad.index(keypad[5]))

no_right_move = [1,4,9,12,13]
no_left_move = [1,2,5,10,13]
no_up_move = [1,2,4,5,9]
no_down_move = [5,10,12,13]

up_special = [3,13]
down_special = [1,11]

for line in lines:
    line = list(line)
    for char in line:
        if char == 'U':
            if position not in no_up_move:
                if position in up_special:
                    position -= 2
                else:
                    position -= 4

        if char == 'D':
            if position not in no_down_move:
                if position in down_special:
                    position += 2
                else:
                    position += 4

        if char == 'R':
            if position not in no_right_move:
                position += 1

        if char == 'L':
            if position not in no_left_move:
                position -= 1    

    letters = [10,11,12,13]
    if position in letters:
        if position == 10:
            code.append('A')   
        if position == 11:
            code.append('B')
        if position == 12:
            code.append('C')
        if position == 13:
            code.append('D')
    else:            
        code.append(position)
bathroom_code = ""

for i in code:
    bathroom_code += str(i)

print(bathroom_code)