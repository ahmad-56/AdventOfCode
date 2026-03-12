user_input = """+1
-2
+3
+1"""

current_frequency = 0
splited = user_input.splitlines()

for i in splited:
    symbol = i[0]
    if symbol == '+':
        current_frequency += int(i[1:])
    elif symbol == '-':
        current_frequency -= int(i[1:])

print(f"New Frequency: {current_frequency}")

#score = 3