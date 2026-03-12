import re
user_input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
#mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
#mul(X,Y)

score = 0

for match in re.finditer(r"mul\((\d+),(\d+)\)", user_input):
    multi = int(match.group(1)) * int(match.group(2))
    score += multi

print(f"score: {score}")

#score = 161