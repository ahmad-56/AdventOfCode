user_input = """123123"""

match = []
checked = []
total = 0

n = len(user_input)
jump = int(n / 2)

while (int(len(checked)/2)) != n:
    for index, i in enumerate(user_input):
        if index >= n - jump:
            index -= n
        if i not in checked:
            if user_input[index] == user_input[index + jump]:
                match.append(int(i))

        if index > 0:
            checked.append(index)
            checked.append(index - n)
        if index < 0:
            checked.append(index)
            checked.append(index + n)
        if index == 0:
            checked.append(index)
            checked.append(index - n)
        
for num in match:
    total += num

print(f"Solution: {total}")