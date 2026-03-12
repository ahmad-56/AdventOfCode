from input import user_input
lines = user_input.splitlines()
array = []
for line in lines:
    line = line.split()
    array.append(line)
grand_total = 0
total_array = []
for i in range(len(line)):
    total_a = 0
    total_m = 1
    temp = []
    for j in range(len(array)):
        temp.append(array[j][i])
    operator = temp[-1]
    if operator == "*":
        for i in range(len(temp)-1):
            total_m *= int(temp[i])
        total_array.append(total_m)
    elif operator == "+":
        for i in range(len(temp)-1):
            total_a += int(temp[i])
        total_array.append(total_a)
for num in total_array:
    grand_total += num
print(grand_total)