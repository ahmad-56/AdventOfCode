carate_order = """        [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 """

lines = carate_order.splitlines()
crate_rows = lines[:-1]
for i in crate_rows:
    array = i.split(' ')

print(array[6][3])