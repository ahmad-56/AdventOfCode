from input import user_input

#power consumption can then be found by multiplying the gamma rate by the epsilon rate.
lines = user_input.splitlines()
gamma_rate_list = []

for i in range(len(lines[0])):
    bits_at_position = []
    for line in lines:
        bits_at_position.append(line[i]) 

    if bits_at_position.count('0') > bits_at_position.count('1'):
        gamma_rate_list.append(0)
    else:
        gamma_rate_list.append(1)

gamma_rate_val = "".join(str(num) for num in gamma_rate_list)
dec_val_gam = int(gamma_rate_val, 2)

epsilon_rate_list = []
splited = list(gamma_rate_list)
for i in splited:
    if i == 1:
        epsilon_rate_list.append(0)
    elif i == 0:
        epsilon_rate_list.append(1)

epsilon_rate_val = "".join(str(num) for num in epsilon_rate_list)
dec_val_eps = int(epsilon_rate_val, 2)

power_val = dec_val_gam * dec_val_eps
print(f"Power Value: {power_val}")