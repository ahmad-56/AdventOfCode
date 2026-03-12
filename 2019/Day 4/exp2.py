import re
user_input = [112223, 144434, 144456, 111111, 122122, 334455, 899999]

#Two adjacent digits are the same (like 22 in 122345) but should not be part of a big group
#Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679)

new_list = []

splited = (map(str, user_input))

pattern = r"((?<!\d)(\d)\2(?!\2))"

for num in splited:
    matches = re.findall(pattern, num)  
    if matches:                        
        new_list.append(num)

list_2 = []

for i in new_list:
    all_inc = True
    number = list(i)

    for digit in range(len(number)-1):
        next_dig = number[digit + 1] 
        current_dig = number[digit]
        if current_dig > next_dig:
            all_inc = False
    
    if all_inc:    
        list_2.append(i)

print(f"Possible Passwords = {len(list_2)}")