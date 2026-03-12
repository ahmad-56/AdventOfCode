user_input = """   98  280  652
  396  371  290
  314  477  454
  368  692  564
   48  263  586
  356  902  922"""

triangles = 0
splited = user_input.splitlines()
for i in splited:
    lines = i.split()
    int_list = list(map(int, lines))

    for i in range(len(splited)):
        for j in range(len(int_list)):
            print(int_list[0][0])