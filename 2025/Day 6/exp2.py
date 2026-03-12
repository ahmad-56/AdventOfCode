user_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +"""
lines = user_input.splitlines()
array = []
for line in lines:
    line = line.split()
    array.append(line)
num1 = ""
grand_total = 0
total_array = []
for i in range(len(line)):
    total_a = 0
    total_m = 1
    temp = []
    temp2 = []
    for j in range(len(array)):
        temp.append(array[j][i])
    operator = temp[-1]
    for i in temp:
        temp2.append(list(i))
    new_temp = [len(x) for x in temp]
    length = max(new_temp)
    for row in range(3):
        for col in range(length, 0, -1):    
            print(temp2[row][col])