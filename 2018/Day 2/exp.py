user_input = """abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab"""
new_list_1 = []
new_list_2 = []

splited = user_input.splitlines()
for i in splited:
    lines = list(i)
    counts = set()
    for i in lines:
        counted = lines.count(i)
        counts.add(counted)
    
    for i in counts:
        if i == 2:
            new_list_1.append(2)
        if i == 3:
            new_list_2.append(3)      

num_1 = new_list_1.count(2) # should be 4
num_2 = new_list_2.count(3) # should be 3
print(num_1)
print(num_2)

checksum = num_1 * num_2
print(f"Checksum = {checksum}")

# checksum = 12