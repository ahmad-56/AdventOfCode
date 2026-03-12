# snd X plays a sound with a frequency equal to the value of X.
# set X Y --> X = Y
# add X Y --> X = X + Y
# mul X Y --> X = X * Y
# mod X Y --> X = remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
# rcv X  --> recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
# jgz X Y --> jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

user_input = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

lines = user_input.splitlines()
register_list = []
for i in lines:
    line = i.split()
    operator = int(line[0])
    register = int(line[1])
    num = int(line[2])

    register_list.append(register)
    if operator == "set":
        register = num
    if operator == "add":
        register += num
    if operator == "mul":
        register = register * num
    if operator == "mod":
        register = register % num
    if operator == "snd":
        send = register
        print(f"{register}")
    if operator == "rcv":
        if register != 0:
            register = send
#    if operator == "jgz"

print(register_list)
