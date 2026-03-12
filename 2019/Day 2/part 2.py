from input import user_input
#1: input + input
#2: input * input
#99: Halt the program
splited = list(map(int, user_input.split(',')))

splited[1] = 12
splited[2] = 2
found = False


for noun in range(100):
    if found:
        break
    for verb in range(100):
        if found:
            break
        splited = list(map(int, user_input.split(',')))
        splited[1] = noun
        splited[2] = verb
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

        if splited[0] == 19690720:
            calculated = (100 * noun) + verb
            print(f"Noun: {noun}")
            print(f"Verb: {verb}")
            print(splited[0]) # Output: 19690720
            print(f"Ans: {calculated}")
            found = True