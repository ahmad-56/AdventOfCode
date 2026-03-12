import re
user_input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
#mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
#mul(X,Y)
# do() and don't()
score = 0
enabled = False

for match in re.search(r"[do()][don't()]", user_input):
    if re.finditer():
        for match in re.finditer(r"mul\((\d+),(\d+)\)", user_input):
            multi = int(match.group(1)) * int(match.group(2))
            score += multi

print(f"score: {score}")

#score = 48