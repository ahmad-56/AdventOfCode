from input import user_input

splited = user_input.split('\n\n')
calculated = []

for i in splited:
    groups = i.splitlines()
    added = 0
    for i in groups:
        added += int(i)
    calculated.append(added)

largest = []
while len(largest) < 3:
    biggest = max(calculated)
    largest.append(biggest)
    calculated.remove(biggest)

print(f"LARGEST: {largest}")
total = 0
for i in largest:
    total += i

print(f"Largest Values: {total}")