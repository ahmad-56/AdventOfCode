import re
user_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

lines = user_input.splitlines()
answer_array = []
num_array = []
for line in lines:
    collon_in = line.index(":")
    answer = line[:collon_in]
    answer_array.append(answer)
    line = line.split(" ")
    lines.remove(line[0])
    for n in range(1, len(line)):
        num_array.append(line[n])
print(lines)
print(answer_array)
print(num_array)