from input import user_input

splited = user_input.splitlines()
column_1 = []
column_2 = []

for i in splited:
    rows = i.split()
    column_1.append(int(rows[0]))
    column_2.append(int(rows[1]))

total = 0

for i in range(0, len(column_1)):
    counts = column_2.count(column_1[i])
    score = column_1[i] * counts
    total += score

print(f"total: {total}")