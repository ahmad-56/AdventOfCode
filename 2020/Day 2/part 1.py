from input import user_input

passwords = 0

splited = user_input.splitlines()
for i in splited:
    parts = i.split()
    math_values = parts[0].split('-')
    check_alpha = parts[1].replace(':', '')

    min_value = int(math_values[0])
    max_value = int(math_values[1])

    counted_alpha = int(parts[2].count(check_alpha))
    if min_value <= counted_alpha and counted_alpha <= max_value:
        passwords += 1

print(f"Number of Correct Passwords: {passwords}")