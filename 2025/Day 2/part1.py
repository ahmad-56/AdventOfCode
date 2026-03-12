from input import user_input

lines = user_input.split(",")
invalid = 0
for line in lines:
    line = line.split("-")
    first_ID = line[0]
    last_ID = line[-1]
    
    for num in range(int(first_ID), int(last_ID) + 1):
        num = str(num)
        mid_ID = int((len(num))/2)
        check1 = num[0:mid_ID]
        check2 = num[mid_ID:]

        if check1 == check2:
            invalid += int(num)
            
print(f"Sum of invalid IDS: {invalid}")