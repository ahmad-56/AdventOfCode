#rules:
    #at least three vowels (aeiou only)
    #at least one letter that appears twice in a row, like xx
    #does not contain the strings ab, cd, pq, or xy

import re

user_input = """ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb"""

splitted = user_input.splitlines()

pattern = r"(ab|cd|pq|xy)"

new_list = []
for i in splitted:
    if not re.search(pattern, i):
        new_list.append(i)

pattern = r"[aeiou]"

new_list_2 = []
for i in new_list:
    vowel_count = len(re.findall(pattern, i))
    if vowel_count >= 3:
        new_list_2.append(i)

pattern = r"(.)\1"

new_list_3 = []
for i in new_list_2:
    if re.search(pattern, i):
        new_list_3.append(i)

nice = int(len(new_list_3))
print(f"Nice: {nice}") #2