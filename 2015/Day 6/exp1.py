from gridfile import grid
import re

user_input = """toggle 461,550 through 564,900
turn off 370,39 through 425,839
turn off 464,858 through 833,915"""

grid_1 = grid()

splited = user_input.splitlines()
code_words = r"(toggle|turn off|turn on)"

for i in splited:
    pattern = r"(\d+),(\d+)\s+through\s+(\d+),(\d+)"
    match = re.search(pattern, i)
    if match:
        x1, y1, x2, y2 = map(int, match.groups())

    code_word = re.search(code_words, i)
    if code_word:  
        word = code_word.group(0)
        if word == "toggle":
            for i in range([x1][y1], [x2][y2]):
                if i == 0:
                    i + 1
                elif i == 1:
                    i - 1
        elif word == "turn off":
            print("turn off")
        elif word == "turn on":
            print("turn on")
