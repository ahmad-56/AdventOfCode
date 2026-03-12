from input import user_input
coords = []
lines = user_input.splitlines()
for line in lines:
    x, y = map(int, line.split(","))
    coords.append((x,y))
area_array = []
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        width = abs(y2 - y1)
        length = abs(x2 - x1)
        area = (width * length) + width + length + 1
        area_array.append(area)
largest_area = max(area_array)
print(f"Largest Area: {largest_area}")