carate_order = """    
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 """

user_input = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

splited = user_input.splitlines()
for i in splited:
    line = []
    groups = i.split(' ')
    numeric_values = []
    for i in groups:
        if i.isnumeric():
            numeric_values.append(i)
    
    count_to_move = int(numeric_values[0])
    val_from = int(numeric_values[1])
    val_to = int(numeric_values[2])
