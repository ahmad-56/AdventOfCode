user_input ="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

splited = user_input.splitlines()
corrected = 0

for i in splited:
    line = []
    groups = i.split(',')
    for i in groups:
        groups = i.split('-')
        line.append(groups)

    min_val_1 = int(line[0][0])
    max_val_1 = int(line[0][1]) + 1
    min_val_2 = int(line[1][0])
    max_val_2 = int(line[1][1]) + 1

    list_a = []
    for i in range(min_val_1, max_val_1):
        list_a.append(i)
    list_b = []
    for i in range(min_val_2, max_val_2):
        list_b.append(i)    

    set_a = set(list_a)
    set_b = set(list_b)

    if not set_a.isdisjoint(set_b) or not set_b.isdisjoint(set_a):
        corrected +=1

print(f"Answer: {corrected}")