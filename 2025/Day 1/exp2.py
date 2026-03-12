user_input = """L999
R10
R1"""
"""L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

array = []
for i in range(-1,99):
    array.append(i+1)

count = 0
position = 50
pos = 0
lines = user_input.splitlines()

#movement number
for line in lines: 
    condition = line[0]
    movement = line [1:]
    num1 = 0
#conditions
    if condition == "R":    #condition
        pos = position + int(movement)  #new position
        pos_str = str(pos)  #for string manipluation
        
        # numbers from 99 to 999
        if pos > 99 and pos <= 999:
            num1 = pos_str[0]
            pos -= (int(num1)*100)
            
        # numbers greater than 999    
        if pos > 999:
            num1 = pos_str[0:2]
            pos -= (int(num1)*100)     
        
        # numbers from -999 to -99
        if pos >= -999 and pos <= -99:
            num1 = pos_str[1]
            pos += (int(num1)*100)

        # numbers less than -999
        if pos < -999:
            num1 = pos_str[1:3]
            pos += (int(num1)*100)

        #after everything is completly checked
        count += int(num1)

        # numbers from -99 to 99 and not 0
        if (pos > 0 and pos <= 99) or (pos>= -99 and pos < 0):        
            for i in range(pos, position): 
                if i == 0:
                    count +=1
                    break
            position = array[pos]
        if position == 0:
            count += 1
#------------------------------------------------------------------        
    if condition == "L":    #condition
        pos = position - int(movement)  #new position
        pos_str = str(pos)  #for string manipluation
        
        # numbers from 99 to 999
        if pos > 99 and pos <= 999:
            num1 = pos_str[0]
            pos -= (int(num1)*100)
            
        # numbers greater than 999    
        if pos > 999:
            num1 = pos_str[0:2]
            pos -= (int(num1)*100)     
        
        # numbers from -999 to -99
        if pos >= -999 and pos <= -99:
            num1 = pos_str[1]
            pos += (int(num1)*100)

        # numbers less than -999
        if pos < -999:
            num1 = pos_str[1:3]
            pos += (int(num1)*100)

        #after everything is completly checked
        count += int(num1)

        # numbers from -99 to 99 and not 0
        if (pos > 0 and pos <= 99) or (pos>= -99 and pos < 0):        
            for i in range(pos, position): 
                if i == 0:
                    count +=1
                    break
        position = array[pos]
        if position == 0:
            count += 1
print(f"Password: {count}") #6