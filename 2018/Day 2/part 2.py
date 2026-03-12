from input import user_input

splited = user_input.splitlines()
found = False

for i in range(len(splited)):
    if found:
        break
    for j in range(i + 1, len(splited)):
        line1 = list(splited[i])
        line2 = list(splited[j])
        common_list = []
        for k in range(len(line1)):
            if line1[k] == line2[k]:
                common_list.append(line1[k])

        if len(common_list) == len(line1) - 1:
            answer = common_list
            found = True
            break   # break inner loop

corrected_answer = "".join(answer)
print(f"ans: {corrected_answer}")