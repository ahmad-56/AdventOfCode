user_input = """aa bb cc dd ee 
aa bb cc dd aa
aa bb cc dd aaa"""

lines = user_input.splitlines()
total_valid = len(lines)

for line in lines:
    words = line.split()
    for word in words:
        counted = words.count(word)
    if counted > 1:
        total_valid -= 1

print(f"Total Valid Phrases: {total_valid}") #2