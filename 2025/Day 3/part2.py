#from input import user_input
user_input = """987654321111111
811111111111119
234234234234278
818181911112111"""
banks = user_input.splitlines()
total_joltage_output = 0 
count = 0
for bank in banks:
    bank = list(bank)
    temparray = []
    count = 0
    for i in range(len(bank)):
        if bank[i] < bank[i+1]:

            while count < 12: 
                for j in range(i+1, len(bank)):
                    num += bank[j]
                    count += 1
            print(num)