from input import user_input

#find the two numbers that add up to 2020 and multiply them to find answer

splited = list(map(int, user_input.split()))
for i in splited:
    for j in splited:
        if i + j == 2020:
            answer = i*j

print(f"Answer: {answer}")
