from input import user_input

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
} 

for k,v in numbers.items():
    user_input = user_input.replace(k,v)

corrected_list = []
splited = user_input.splitlines()
for i in splited:
    corrected_list.append(i)
    print(corrected_list)

latest_list = []
for line in corrected_list:
    list_one = list(line)
    new_list = []
    print(list_one)

    for i in list_one:
        if not i.isalpha():
            new_list.append(i)
    print(new_list)

    updated_list = []
    for i in new_list:
        updated_list.append(new_list[0])
        updated_list.append(new_list[-1])
        print(updated_list)
        break

    combined_number = updated_list[0] + updated_list[-1]    
    latest_list.append(combined_number)
    print(combined_number)

total = 0
user_message_tostart = input("Type start: ").lower()
if user_message_tostart == 'start':
    for i in latest_list:
        total += int(i)
    print(f"The total is: {total}")
user_message = input("").lower()




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
    for i in range(1, len(line)+1):
        check_word = line[:i]
        for k,v in numbers.items():
             updated_input = user_input.replace(k,v)

splited_2 = updated_input.splitlines()
latest_list = []
for i in splited_2:
    list_one = list(i)
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
    latest_list.append(combined_number)

    total = 0
    
for i in latest_list:
    total += int(i)
print(f"The total is: {total}")
#score = 281