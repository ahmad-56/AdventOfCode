user_input = """nqninenmvnpsz874
8twofpmpxkvvdnpdnlpkhseven4ncgkb
six8shdkdcdgseven8xczqrnnmthreecckfive
"""

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}



onlynum_list = []
splited_lines = user_input.splitlines()
print(splited_lines)
for line in splited_lines:
    edited = numbers.get(line, 'error')
    onlynum_list.append(edited)
print(onlynum_list)
