from input import user_input

splited = user_input.split(',')
numbers = list(map(int, splited))
count = 0

timer_counts = []
for i in range(1, 10):
    timer_counts.append(0)

while count < 256:
    new_list = []
    for i in range(len(numbers)):
        if numbers[i] == 0:
            new_list.append(6)
            new_list.append(8)  
        else:
            new = numbers[i] - 1
            new_list.append(new)

print(f"Fish Count: {len(new_list)}")
#After 80 Days - Fish count = 5934