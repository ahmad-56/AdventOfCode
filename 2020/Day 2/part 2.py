from input import user_input

passwords = 0

splited = user_input.splitlines()
for i in splited:
    parts = i.split()
    math_values = parts[0].split('-')
    check_alpha = parts[1].replace(':', '')

    min_value = int(math_values[0]) - 1
    max_value = int(math_values[1]) - 1 
    values = parts[2]

    if (check_alpha == values[min_value]) ^ (check_alpha == values[max_value]):
        passwords += 1

print(f"Number of Correct Passwords: {passwords}")