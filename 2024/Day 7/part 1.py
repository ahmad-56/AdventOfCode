import re
user_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

lines = user_input.splitlines()
ans_plus = 0
ans_mul = 0
for line in lines:
    nums = line.replace(":", "").split()
    nums = list(map(int, nums))
    answer = nums[0]
    
    for n in range(1, len(nums)):
        ans_plus += nums[n]
        ans_mul *= nums[n]
    print(ans_plus)
    print(ans_mul) 