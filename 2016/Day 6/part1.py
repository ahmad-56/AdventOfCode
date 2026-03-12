from input import user_input

splited_lines = user_input.splitlines()
letters = []

for i in splited_lines:
    total_col = len(list(i))

for i in range(0,int(total_col)):
    col = []
    counts = []
    for lines in splited_lines:
        line = list(lines)
        total_col = len(line)
        col.append(line[int(i)])
    for i in col:
        counted = col.count(i)
        counts.append(counted)
    max_counts = max(counts)
    place = counts.index(max_counts)
    letter = col[place]
    letters.append(letter)

coded_password = ""
for i in letters:
    coded_password += i
print(f"code: {coded_password}")