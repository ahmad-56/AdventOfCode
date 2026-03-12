from input import user_input

increased = 0
splited = user_input.splitlines()

for i in range(len(splited) - 1):
    val_1 = int(splited[i])
    val_2 = int(splited[i+1])
    if val_2 > val_1:
        increased += 1

print(f"no. increased: {increased}")