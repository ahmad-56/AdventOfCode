from input import user_input

splited = user_input.splitlines()
forward = 0
depth = 0

for i in splited:
    word, value = i.split()
    if word == 'forward':
        forward += int(value)
    elif word == 'up':
        depth -= int(value)
    elif word == 'down':
        depth += int(value)

calculated = forward * depth

print(f"Ans: {calculated}")