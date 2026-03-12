checking_list = [-1, -2, -2, -1]
safe = 0
print(checking_list)

for i in checking_list:
    original = checking_list.copy() # backup
    place = checking_list.index(i) # to insert it back
    checking_list.remove(i) # password check
    checker = len(original) # og = 4 new = 3
    for j in checking_list:
        if not -3 <= j < 0:
            original.remove(j)
        
    if len(original) == checker:
            safe += 1
        
    checking_list.insert(place, i)
    
print(checking_list)
print(f"safe: {int(safe/4)}")

# [-1, -2, -2, -1]
# [1, 5, 1, 1]
# [-2, -1, -4, -1]
# [2, -1, 2, 1]
# [-2, -2, 0, -3]
# [2, 3, 1, 2]