from input import user_input

stop_position = 0
total = 0
lines = user_input.splitlines()
for line in lines:
    line_refined = line.split()
    check_list = []
    ans_list = []
    for char in line_refined:
        if char == '|':
            stop_position = line_refined.index(char)
    for i in range(2, stop_position):
        check_list.append(int(line_refined[i]))
    for i in range(stop_position + 1, len(line_refined)):
        ans_list.append(int(line_refined[i]))
    
    check = 0
    ans = 0
    for i in check_list:
        if i in ans_list:
            check += 1
    
    if check != 0:
        ans = 2**(check-1)

    total += ans

print(f"Total points: {total}")