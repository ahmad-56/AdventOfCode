from input import user_input
from dictionaries import dict
#count each item in the line then make 2 groups of them ---> find same occuring alphabet ---> each alphabet has its own value ---> find sum of values

splited = user_input.splitlines()
final_list = []
for i in splited:
    found_in_line = False
    mid = len(i) // 2
    first_half = list(i[:mid])
    second_half = list(i[mid:])
    for i in first_half:
        if not found_in_line:    
            if second_half.count(i) > 0:
                final_list.append(i)
                found_in_line = True

new_list = []
for item in final_list:
    for k, v in dict.items():
        item = item.replace(k, str(v))
    new_list.append(item)

total = 0
for i in new_list:
    total += int(i)
print(f"total: {total}")