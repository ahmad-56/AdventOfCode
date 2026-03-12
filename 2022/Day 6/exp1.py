user_input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
found = False
while not found:
    for position in range(len(user_input),):
        chars = user_input[position:position+4]
        char_list = list(chars)
        count_list = []
        check = [1,1,1,1]
        for i in char_list:
            counts = char_list.count(i)
            count_list.append(counts)
        if count_list == check:
            print(position+4) # 11
            found = True
        if found:
            break