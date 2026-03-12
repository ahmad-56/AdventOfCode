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
        new_list = checking_list.copy()
        for i in checking_list:
            place = new_list.index(i) # to insert it back
            new_list.remove(i) # password check
            checker_2 = len(new_list) # og = 4 new = 3
            for j in new_list:
                if not -3 <= j < 0:
                    new_list.remove(j)
                
            if len(new_list) == checker_2:
                    safe += 1
                
        checking_list.insert(place, i)

    elif inc == checker:
        print("all inc")
        for i in checking_list:
            new_list = checking_list.copy() # backup
            place = new_list.index(i) # to insert it back
            new_list.remove(i) # password check
            checker_2 = len(new_list) # og = 4 new = 3
            for j in new_list:
                if not 0 < j <= 3:
                    new_list.remove(j)
                
            if len(new_list) == checker_2:
                    safe += 1
                
        checking_list.insert(place, i)        
    else:
        print("delete")

print(f"safe: {int(safe)}")