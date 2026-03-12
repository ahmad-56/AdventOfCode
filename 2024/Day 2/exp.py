user_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

splited = user_input.splitlines()
safe = 0

for i in splited:
    listed = i.split()
    rows = [int(i) for i in listed]
    checking_list = []

    for i in range(len(rows) - 1):
        checking_list.append(rows[i+1] - rows[i])
        checker = len(checking_list)
    dec = 0
    inc = 0
    for i in checking_list:
        while True:
            if i < 0:
                dec += 1
            break  
        while True: 
            if i > 0:
                inc += 1
            break

    if dec == checker:
        print("all dec")
        for i in checking_list:    
            if not -3 <= i < 0:
                checking_list.remove(i)
        if len(checking_list) == checker:
            safe += 1
    elif inc == checker:
        print("all inc")
        for i in checking_list:    
            if not 0 < i <= 3:
                checking_list.remove(i)
        if len(checking_list) == checker:
            safe += 1
    else:
        print("delete")
print(f"safe: {safe}")