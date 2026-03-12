user_input = """3,4,3,1,2"""

splited = user_input.split(',')
numbers = list(map(int, splited))
count = 0

while count < 80:
    new_list = []
    for i in range(len(numbers)):
        if numbers[i] == 0:
            new_list.append(6)
            new_list.append(8)  
        else:
            new = numbers[i] - 1
            new_list.append(new)
    count += 1
    numbers = new_list
print(f"Fish Count: {len(new_list)}")
#After 80 Days - Fish count = 5934
