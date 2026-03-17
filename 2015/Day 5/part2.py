from input import user_input
import re

splitted = user_input.splitlines()

pattern_1 = re.compile(r"(..).*\1")
pattern_2 = re.compile(r"(.).\1")

nice = []

for i in splitted:
    if pattern_1.search(i) and pattern_2.search(i):
        nice.append(i)

nice_words = int(len(nice))
print(f"Nice: {nice_words}")