from input import user_input

splited = user_input.split('\n\n')
calculated = []

for i in splited:
    groups = i.splitlines()
    added = 0
    for i in groups:
        added += int(i)
    calculated.append(added)

largest = max(calculated)
print(f"Largest Value: {largest}")