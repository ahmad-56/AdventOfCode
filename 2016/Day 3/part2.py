from input import user_input

triangles = 0
splited = user_input.splitlines()
for i in splited:
    lines = i.split()
    int_list = list(map(int, lines))

