user_input = """2x3x4"""
#formula = (w + w + l + l) + (l*w*h)
area_list = []

splited = user_input.splitlines()
for i in splited:
    lines = list(map(int, i.split('x')))
    lines.sort()
    print(lines)
    l = lines[0]
    w = lines[1]
    h = lines[2]
    V1 = int(l) * int(w) * int(h)
    P1 = (2 * l) + (2 * w)
    total_area = int(P1) + int(V1)
    area_list.append(total_area)

total = 0
for i in area_list:
        total += int(i)
print(f"The total is: {total}")