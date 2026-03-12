from input import user_input
lines = user_input.splitlines()
total = 0

index = lines.index("") 
num_array = lines[index+1:]
range_array = lines[:index]

fresh_ids = set()

ranges = []
for r in range_array:
    start, end = map(int, r.split("-"))
    ranges.append((start, end))

for j in num_array:
    num = int(j)
    for start, end in ranges:
        if start <= num <= end:
            total += 1
            fresh_ids.add(num)
            break

print(total)