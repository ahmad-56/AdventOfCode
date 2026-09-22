user_input = """91212129"""

user_input = list(user_input)
match = []
total = 0
for i in range(len(user_input)-1):
    if user_input[i] == user_input[i+1]:
        match.append(user_input[i])
if user_input[-1] == user_input[0]:
    match.append(user_input[0])

for n in match:
    total += int(n)

print(f"Solution: {total}")