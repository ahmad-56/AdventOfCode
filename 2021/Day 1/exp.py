user_input = """199
200
208
210
200
207
240
269
260
263"""

increased = 0
splited = user_input.splitlines()
new_list = []

for i in range(len(splited) - 2):
    val_1 = int(splited[i])
    val_2 = int(splited[i+1])
    val_3 = int(splited[i+2])

    new_sum = val_1 + val_2 + val_3
    new_list.append(new_sum)

for i in range(len(new_list) - 1):
    val_1 = int(new_list[i])
    val_2 = int(new_list[i+1])
    if val_2 > val_1:
        increased += 1 

print(f"no. increased: {increased}")
#score = 5