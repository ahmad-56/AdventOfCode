user_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

#power consumption can then be found by multiplying the gamma rate by the epsilon rate.
lines = user_input.splitlines()
new_list = []
list_for_max = []

for digit in range(len(lines[0])):
    bits_at_position = []
    for line in range(len(lines)):
        checker = lines[int(line)][digit]
        bits_at_position.append(lines[int(line)][digit])
       
        if bits_at_position.count('0') > bits_at_position.count('1'):
            if checker == '0':
                new_list.append(lines[line])
            else:
                new_list.append(lines[line])
    
print(new_list)
#multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230