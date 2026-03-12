user_input = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz"""

splited = user_input.splitlines()

lines = [set(line) for line in splited]   # make lines

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        new_lines = lines[i] & lines[j]
        
        if len(new_lines) == len(lines[0]) - 1:
            answer = new_lines

corrected_answer = ""

for i in answer:
    corrected_answer += i


print(f"ans: {corrected_answer}")
print(f"ans: fgij")
#ans: fgij