from input import user_input

#A for Rock, B for Paper, and C for Scissors. 
#X for Rock, Y for Paper, and Z for Scissors
#1 for Rock, 2 for Paper, and 3 for Scissors
#0 if you lost, 3 if the round was a draw, and 6 if you won
points = 0

splited = user_input.splitlines()
for i in splited:
    groups = i.split(' ')
    elf_move = groups[0]
    your_move = groups[1]
    if elf_move == 'A':
        if your_move == 'X':
            points += 1 # for move
            points += 3 # for draw
        elif your_move == 'Y':
            points += 2 # for move
            points += 6 # for victory
        elif your_move == 'Z':
            points += 3 # for move
            points += 0 # for loss
    if elf_move == 'B':
        if your_move == 'X':
            points += 1 # for move
            points += 0 # for loss
        elif your_move == 'Y':
            points += 2 # for move
            points += 3 # for draw
        elif your_move == 'Z':
            points += 3 # for move
            points += 6 # for victory
    if elf_move == 'C':
        if your_move == 'X':
            points += 1 # for move
            points += 6 # for victory
        elif your_move == 'Y':
            points += 2 # for move
            points += 0 # for loss
        elif your_move == 'Z':
            points += 3 # for move
            points += 3 # for draw
        
print(f"Total score: {points}")