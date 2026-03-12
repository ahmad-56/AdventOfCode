#from input import user_input

user_input = """.@.
@@.
..@"""

linez = user_input.splitlines()
lines = []
for line in linez:    
    elements = list(line)
    elements.insert(0,"0")
    elements.append("0")
    lines.append(elements)
padding = list("0"*int(len(line)+2))
lines.append(padding)
lines.insert(0, padding)
for line in lines:
    print("".join(line))
    
