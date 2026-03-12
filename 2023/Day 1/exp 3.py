import re
user_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

numbers = {
    "nine": "9",
    "eight": "8",
    "seven": "7",
    "six": "6",
    "five": "5",
    "four": "4",
    "three": "3",
    "two": "2",
    "one": "1",
    "zero": "0"
}

#corrected input


splited = user_input.splitlines()
for line in splited:
    for start in range(len(line)):
        for end in range(start + 1, len(line) + 1):
            substring = line[start:end]
            for k, v in numbers.items():
                updated_input = substring.replace(k,v)

print(updated_input)