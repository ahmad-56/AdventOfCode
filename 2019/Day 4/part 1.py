import re
from input import user_input

#Two adjacent digits are the same (like 22 in 122345).
#Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679)

new_list = []

splited = list(map(str, user_input))
pattern = r"(11|22|33|44|55|66|77|88|99)"

for num in splited:
    if re.search(pattern, num):
        new_list.append(num)

list_2 = []

for i in new_list:
    all_inc = True
    number = list(i)
    count = 0
    for digit in range(len(number)-1):
        next_dig = number[digit + 1] 
        current_dig = number[digit]
        if current_dig > next_dig:
            all_inc = False
    
    if all_inc:    
        list_2.append(i)

print(f"Possible Passwords = {len(list_2)}")