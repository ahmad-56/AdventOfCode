from input import user_input

splited = user_input.splitlines()
checksum = 0
for i in splited:
    lines = i.split('\t')
    int_list = list(map(int, lines))
    
    num_1 = max(int_list)
    num_2 = min(int_list)

    difference = num_1 - num_2

    checksum += difference    

print(f"Checksum: {checksum}")