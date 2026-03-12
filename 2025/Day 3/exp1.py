user_input = """987654321111111
811111111111119
234234234234278
818181911112111"""
banks = user_input.splitlines()
total_joltage_output = 0
for bank in banks:
    bank = list(bank)
    temparray = []
    for i in range(len(bank)):
        for j in range(i+1, len(bank)):
            num = bank[i] + bank[j]
            temparray.append(int(num))
    joltage = max(temparray)
    total_joltage_output += joltage
print(total_joltage_output) #357