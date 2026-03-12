user_input = "234234234234278"
"""987654321111111
811111111111119
234234234234278
818181911112111"""

banks = user_input.splitlines()
total_joltage_output = 0
joltage_array = []
for bank in banks:
    length = len(bank)
    bank = list(bank)
    count = 0
    num = ""
    for i in bank:
        while count < (length - 12):    
            bank.remove(min(bank))
            count += 1
    for i in bank:
        num += i
    joltage = int(num)
    total_joltage_output += joltage
print(total_joltage_output) #3121910778619
#987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619