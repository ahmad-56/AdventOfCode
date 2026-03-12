# snd X plays a sound with a frequency equal to the value of X.
# set X Y --> X = Y
# add X Y --> X = X + Y
# mul X Y --> X = X * Y
# mod X Y --> X = remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
# rcv X  --> recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
# jgz X Y --> jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

from input import user_input

lines = user_input.splitlines()
register_list = []
for i in lines:
    line = i.split()
    operator = line[0]
    register = line[1]
    #num = line[2]
    if register not in register_list:
        register_list.append(register)
    
print(register_list)