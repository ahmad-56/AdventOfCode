user_input ="""forward 5
down 5
forward 8
up 3
down 8
forward 2"""

splited = user_input.splitlines()
forward = 0
depth = 0
aim = 0

for i in splited:
    word, value = i.split()
    if word == 'forward':
        forward += int(value)
        val_1 = aim * int(value)
        depth += val_1
    elif word == 'up':
        aim -= int(value)
    elif word == 'down':
        aim += int(value)

calculated = forward * depth

print(f"Ans: {calculated}")