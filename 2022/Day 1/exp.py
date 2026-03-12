user_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

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

total = 0
for i in largest:
    total += i

print(f"Largest Value: {total}")