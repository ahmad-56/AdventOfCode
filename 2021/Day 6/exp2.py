user_input = """3,4,3,1,2"""

splited = user_input.split(',')
numbers = list(map(int, splited))
count = 0

timer_counts = [0] * 9

while count < 256:
    for n in numbers:
        timer_counts[n] += 1
        new_fish = timer_counts[0]  # fish with timer 0 create new ones
        timer_counts = timer_counts[1:] + [new_fish]  # shift all timers down, add new fish at 8
        timer_counts[6] += new_fish  # reset timer 0 fish to 6
    count += 1

fish_count = 0

for i in timer_counts:
    fish_count += i
print(fish_count)
print(26984457539)