from input import user_input

lines = user_input.splitlines()
total_valid = len(lines)

for line in lines:
    words = line.split()
    counts = []
    for word in words:
        counted = words.count(word)
        counts.append(counted)
    if max(counts) > 1:
        total_valid -= 1

print(f"Total Valid Phrases: {total_valid}")