user_input = """987654321111111
811111111111119
234234234234278
818181911112111"""

banks = user_input.splitlines()
total_joltage_output = 0
joltage_array = []
temp = 0
for bank in banks:
    n = len(bank)
    bank = list(bank)
    for a in range(0, n-11):
        for b in range(a+1, n-10):
            for c in range(b+1, n-9):
                for d in range(c+1, n-8):
                    for e in range(d+1, n-7):
                        for f in range(e+1, n-6):
                            for g in range(f+1, n-5):
                                for h in range(g+1, n-4):
                                    for i in range(h+1, n-3):
                                        for j in range(i+1, n-2):
                                            for k in range(j+1, n-1):
                                                for l in range(k+1, n):
                                                    number = (
                                                        bank[a] + bank[b] + bank[c] +
                                                        bank[d] + bank[e] + bank[f] +
                                                        bank[g] + bank[h] + bank[i] +
                                                        bank[j] + bank[k] + bank[l]
                                                    )
    if int(number) > temp:
        temp = int(number)
    print(temp)
    total_joltage_output += temp
print(total_joltage_output) #3121910778619        