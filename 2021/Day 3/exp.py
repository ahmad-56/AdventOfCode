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
gamma_rate_list = []

for i in range(len(lines[0])):
    bits_at_position = []
    for line in lines:
        bits_at_position.append(line[i]) 
    if bits_at_position.count('1') >= bits_at_position.count('0'):
        for line in lines:  
            if line[0] == '1':
                print(line)
