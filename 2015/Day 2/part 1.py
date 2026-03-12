from input import user_input
#formula = (2*l*w + 2*w*h + 2*h*l) + (2*a)
area_list = []

splited = user_input.splitlines()
for i in splited:
    lines = i.split('x')
    A1 = int(lines[0]) * int(lines[1])
    A2 = int(lines[1]) * int(lines[2])
    A3 = int(lines[0]) * int(lines[2])
    areas = [A1 , A2 ,A3]
    A4 = min(areas)
    total_area = ((2 * A1) + (2 * A2) + (2 * A3)) + (A4)
    area_list.append(total_area)

total = 0
for i in area_list:
        total += int(i)
print(f"The total is: {total}")