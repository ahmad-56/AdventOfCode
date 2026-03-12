user_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

lines = user_input.splitlines()
total = 0
for line in lines:
    if line == "":
        index = lines.index(line)
        num_array = lines[index+1:]
        range_array = lines[:index]

        fresh_ids = set()

for i in range(len(range_array)):
    nums = range_array[i].split("-")
    ran_s = int(nums[0])
    ran_e = int(nums[-1])
    for j in num_array:
        num = int(j)
        if num not in fresh_ids:
            if ran_s <= num <= ran_e:
                fresh_ids.add(num)
                break
            
print(len(fresh_ids))