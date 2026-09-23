from input import user_input

lines = user_input.splitlines()
total_valid = len(lines)

for line in lines:
    words = line.split()
    checked = False

    for w in range(len(words) - 1):
        if checked:
            break
        for c in range(w + 1, len(words)):
            word1 = words[w]
            word2 = words[c]

            if sorted(word1) == sorted(word2):
                total_valid -= 1
                checked = True
                break

print(f"Total Valid Phrases: {total_valid}")