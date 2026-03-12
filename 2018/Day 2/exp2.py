user_input = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz"""

splited = user_input.splitlines()

for i in range(len(splited)):
    for j in range(i + 1, len(splited)):
        line1 = list(splited[i])
        line2 = list(splited[j])
        common_list = []
        for k in range(len(line1)):
            if line1[k] == line2[k]:
                common_list.append(line1[k])
        if len(common_list) == len(line1) - 1:
            answer = common_list

corrected_answer = ""

for i in answer:
    corrected_answer += i

print(f"ans: fgij")
print(f"ans: {corrected_answer}")
#ans: fgij