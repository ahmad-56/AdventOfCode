from input import user_input
lines = user_input.splitlines()
total = 0

index = lines.index("") 
range_array = lines[:index]

fresh_ids = set()

ranges = []
for r in range_array:
    start, end = map(int, r.split("-"))
    ranges.append((start, end))

for start, end in ranges:
    for num in range(start, end+1):
        fresh_ids.add(num)
        total +=1
print(total)