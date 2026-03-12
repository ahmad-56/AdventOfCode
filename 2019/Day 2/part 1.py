from input import user_input
#1: input + input
#2: input * input
#99: Halt the program

splited = list(map(int, user_input.split(',')))

splited[1] = 12
splited[2] = 2

for i in range(0, len(splited), 4):
    opcode = splited[i]
    if opcode == 99:
        break
    
    input_1_loc = splited[i+1]
    input_2_loc = splited[i+2]
    output_loc  = splited[i+3]

    if opcode == 1:
        splited[output_loc] = splited[input_1_loc] + splited[input_2_loc]
    elif opcode == 2:
        splited[output_loc] = splited[input_1_loc] * splited[input_2_loc]


print(splited)

print(splited[0])