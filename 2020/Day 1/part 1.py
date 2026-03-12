from input import user_input

#find the two numbers that add up to 2020 and multiply them to find answer

splited = list(map(int, user_input.split()))
for i in splited:
    for j in splited:
        for k in splited:
            if i + j + k == 2020:
                answer = i*j*k

print(f"Answer: {answer}")