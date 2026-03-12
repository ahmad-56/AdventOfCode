from input import user_input

current_frequency = 0
splited = user_input.splitlines()
seen_frequencies = set()
found = False

while True:
    for i in splited:
        symbol = i[0]
        if symbol == '+':
            current_frequency += int(i[1:])
        elif symbol == '-':
            current_frequency -= int(i[1:])

        if current_frequency in seen_frequencies:
            print(f"First repeated: {current_frequency}")
            found = True
            break
        else:
            seen_frequencies.add(current_frequency)

    if found:
        break