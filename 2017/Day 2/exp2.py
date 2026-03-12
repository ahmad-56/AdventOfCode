user_input = """5 9 2 8
9 4 7 3
3 8 6 5"""

splited = user_input.splitlines()
checksum = 0
for i in splited:
    lines = i.split('\t')
    int_list = list(map(int, lines))
    
    for i in range(len(int_list)):
        for j in range(i+1, len(int_list)):
            if int_list[i]%int_list[j] == 0:
                num_1 = int_list[i]
                num_2 = int_list[j]
                number = num_1/num_2
            elif int_list[j]%int_list[i] == 0:            
                num_1 = int_list[j]
                num_2 = int_list[i]
                number = num_1/num_2

    checksum += number    

print(f"Checksum: {checksum}")