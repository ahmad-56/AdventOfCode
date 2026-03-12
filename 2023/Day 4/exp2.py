user_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

stop_position = 0
total = 0
lines = user_input.splitlines()
cards = []
for card_num in range(len(lines)):
    cards.append(card_num)
    for line in lines:
        line_refined = line.split()
        check_list = []
        ans_list = []
        for char in line_refined:
            if char == '|':
                stop_position = line_refined.index(char)
        for i in range(2, stop_position):
            check_list.append(int(line_refined[i]))
        for i in range(stop_position + 1, len(line_refined)):
            ans_list.append(int(line_refined[i]))
        
        check = 0
        ans = 0
        for i in check_list:
            if i in ans_list:
                check += 1

        count = 0
        while count < check:
            for card in range(card_num+1, len(cards)):
                card += 1 
                card_num  
            for i in range(len(lines)):
                i

print(f"Total points: {total}") #30