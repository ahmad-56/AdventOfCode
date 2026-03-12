user_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

splited = user_input.splitlines()
digit_lists = []
lower_list = []

for line in splited:
    digits = list(line)
    digit_lists.append(digits)

for line in range(len(digit_lists)):
    for i in range(len(str(line))):
        lower_num_found = True
        current_num = digit_lists[line][i]
        up = digit_lists[line+1][i] 
        down = digit_lists[line-1][i] 
        right = digit_lists[line][i+1] 
        left = digit_lists[line][i-1]
        if current_num >= down or current_num >= right or current_num >= left:
            lower_num_found = False
        if line[0]:
            if current_num >= up or current_num >= down or current_num >= right or current_num >= left:
                lower_num_found = False
        elif line[-1]:
            if current_num >= up or current_num >= right or current_num >= left:
                lower_num_found = False
        if lower_num_found:
            lower_list.append(current_num)

print(lower_list)