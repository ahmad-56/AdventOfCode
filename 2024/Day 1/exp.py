import math
user_input = """3   4
4   3
2   5
1   3
3   9
3   3"""

splited = user_input.splitlines()
column_1 = []
column_2 = []

for i in splited:
    rows = i.split()
    column_1.append(int(rows[0]))
    column_2.append(int(rows[1]))

column_1.sort()
column_2.sort()

total = 0

for i in range(0, len(column_1)):
    distance = abs(column_1[i] - column_2[i])
    total += distance

print(f"total: {total}")
#distance = 11