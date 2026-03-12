import re
from input import user_input

#mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
#mul(X,Y)

score = 0

for match in re.finditer(r"mul\((\d+),(\d+)\)", user_input):
    multi = int(match.group(1)) * int(match.group(2))
    score += multi

print(f"score: {score}")