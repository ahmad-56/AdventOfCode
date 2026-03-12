user_input = """R2, L3"""

array = []
for i in range(10):
    array.append(0)

words = user_input.split(", ")
for word in words:
    condition = word[0]
    movement = word[1:]
    if condition == "R":
        
    elif condition == "L":