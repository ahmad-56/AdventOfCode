from dictionaries import dict

user_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

#count each item in the line then make 2 groups of them ---> find same occuring alphabet ---> each alphabet has its own value ---> find sum of values
#find item that is in every 3 lines ---> find same occuring alphabet ---> each alphabet has its own value ---> find sum of values

lines = user_input.split('\n')
final_list = []

for i in range(0, len(lines), 3):
    group = lines[i:i+3]
    
    line1, line2, line3 = group
    common = set(line1) & set(line2) & set(line3)

    if common:
        final_list.append(common.pop())  

new_list = []
for item in final_list:
    for k, v in dict.items():
        item = item.replace(k, str(v))
    new_list.append(item)

total = 0
for i in new_list:
    total += int(i)
print(f"total: {total}")