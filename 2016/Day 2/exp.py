#U moves up, D moves down, L moves left, and R moves right
user_input = """ULL
RRDDD
LURDL
UUUUD"""

keypad = []
code = []

for i in range(1, 10):
    keypad.append(i)

lines = user_input.splitlines()
position = int(keypad.index(keypad[4]))
no_right_move = [3,6,9]
no_left_move = [1,4,7]
no_up_move = [1,2,3]
no_down_move = [7,8,9]

for line in lines:
    line = list(line)
    for char in line:
        if char == 'U':
            if position not in no_up_move:
                position -= 3

        if char == 'D':
            if position not in no_down_move:
                position += 3
        
        if char == 'R':
            if position not in no_right_move:
                position += 1

        if char == 'L':
            if position not in no_left_move:
                position -= 1    

    code.append(position)   

bathroom_code = ""

for i in code:
    bathroom_code += str(i)

print(bathroom_code) #1985