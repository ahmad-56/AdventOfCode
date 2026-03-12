import re
from input import user_input

#Two adjacent digits are the same (like 22 in 122345) but should not be part of a big group
#Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679)

new_list = []

splited = (map(str, user_input))

pattern = (
    r'(?:(?<!0)00(?!0))|(?:(?<!1)11(?!1))|(?:(?<!2)22(?!2))|'
    r'(?:(?<!3)33(?!3))|(?:(?<!4)44(?!4))|(?:(?<!5)55(?!5))|'
    r'(?:(?<!6)66(?!6))|(?:(?<!7)77(?!7))|(?:(?<!8)88(?!8))|'
    r'(?:(?<!9)99(?!9))'
)

for num in splited:
    matches = re.findall(pattern, num)  
    if matches:                        
        new_list.append(num)

list_2 = []

for i in new_list:
    all_inc = True
    number = list(i)

    for digit in range(len(number)-1):
        next_dig = int(number[digit + 1]) 
        current_dig = int(number[digit])

        if current_dig > next_dig:
            all_inc = False
    
    if all_inc:    
        list_2.append(i)

print(f"Possible Passwords = {len(list_2)}")