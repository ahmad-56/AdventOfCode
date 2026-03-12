user_input = """0
3
0
1
-3"""

#exit reached in 5 steps

lines = user_input.splitlines()

num_list = []
for i in lines:
    num_list.append(int(i))

next_place = 100000

while next_place > len(num_list):
    for i in num_list:
        place = num_list.index(i)
        next_place = place + i
        new_value = i + 1
        num_list[place] = new_value
        print(num_list)