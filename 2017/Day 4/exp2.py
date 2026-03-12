user_input = """abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio"""

lines = user_input.splitlines()
total_valid = len(lines)

for line in lines:
    words = line.split()
    for word in words:
        counted = words.count(word)
        
    if counted > 1:
        total_valid -= 1

print(f"Total Valid Phrases: {total_valid}") #3