from input import user_input
import math

#mass, divide by three, round down, and subtract 2

splited = user_input.splitlines()
values_list = []
fuel_required = 0

for i in splited:
    divided_value = int(i) / 3
    rounded = math.floor(divided_value)
    final_value = rounded - 2
    values_list.append(final_value)

for i in values_list:
    fuel_required += i

print(fuel_required)