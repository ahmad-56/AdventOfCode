user_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

lines = user_input.split(",")
invalid = 0
number = ""

for line in lines:
    line = line.split("-")
    first_ID = line[0]
    last_ID = line[-1]
    
    for num in range(int(first_ID), int(last_ID) + 1):
        no = list(num)
        for i in no:
            number += i

        #invalid += int(num)
            
print(f"Sum of invalid IDS: {invalid}\nAns:4174379265") #4174379265