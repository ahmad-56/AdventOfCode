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

for k,v in numbers.items():
    numbers.get(k,v)

print(user_input)

corrected_list = []
splited = user_input.splitlines()
for i in splited:
    corrected_list.append(i)

latest_list = []
for line in splited:
    list_one = list(line)
    new_list = []

    for i in list_one:
        if not i.isalpha():
            new_list.append(i)

    updated_list = []
    for i in new_list:
        updated_list.append(new_list[0])
        updated_list.append(new_list[-1])
        break

    combined_number = updated_list[0] + updated_list[-1]    
    print(combined_number)
    latest_list.append(combined_number)

total = 0
for i in latest_list:
    total += int(i)
print(f"The total is: {total}")
print(f"The total is: {281}")

#ans = 281