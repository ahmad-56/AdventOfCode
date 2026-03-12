user_input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
found = False
check = []
for i in range(14):
    check.append(1)
while not found:
    for position in range(len(user_input),):
        chars = user_input[position:position+14]
        char_list = list(chars)
        count_list = []
        for i in char_list:
            counts = char_list.count(i)
            count_list.append(counts)
        if count_list == check:
            print(position+14) # 26
            found = True
        if found:
            break