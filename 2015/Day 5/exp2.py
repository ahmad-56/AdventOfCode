#rules:
    #pair of any two letters at least twice but should not overlap: xyxy (xy) or aabcdefgaa
    #at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

import re

user_input = """qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy"""

splitted = user_input.splitlines()

pattern_1 = re.compile(r"(..).*\1")
pattern_2 = re.compile(r"(.).\1")

nice = []

for i in splitted:
    if pattern_1.search(i) and pattern_2.search(i):
        nice.append(i)

nice_words = int(len(nice))
print(f"Nice: {nice_words}") #2