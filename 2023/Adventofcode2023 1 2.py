from input import user_input
from Adventofcode2023 1 import 

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
} 

#corrected input
corrected_list = []
latest_list = []
for k,v in numbers.items():
    user_input = user_input.replace(k,v)

splited = user_input.splitlines()
for line in splited:
    splited_list = list(line)
    new_list = []
    
    for i in splited_list:
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
user_message_tostart = input("Type start: ").lower()
if user_message_tostart == 'start':
    for i in latest_list:
        total += int(i)
    print(f"The total is: {total}")
user_message = input("").lower()

print(new_list)