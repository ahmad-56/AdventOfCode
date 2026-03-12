from input import user_input
array = []
for i in range(-1,99):
    array.append(i+1)

count = 0
position = array.index(50)
pos = 0
lines = user_input.splitlines()

#movement number
for line in lines: 
    condition = line[0]
    movement = line [1:]
    num1 = 0
#conditions
    if condition == "R":    #condition
        pos_str = str(pos)  #for string manipluation
        
        # numbers from 99 to 999
        if pos > 99 and pos <= 999:
            num1 = pos_str[0]
            pos -= (int(num1)*100)
            
        # numbers greater than 999    
        elif pos > 999:
            num1 = pos_str[0:2]
            pos -= (int(num1)*100)     
        
        # numbers from -999 to -99
        elif pos >= -999 and pos <= -99:
            num1 = pos_str[1]
            pos += (int(num1)*100)

        # numbers less than -999
        elif pos < -999:
            num1 = pos_str[1:3]
            pos += (int(num1)*100)

        #after everything is completly checked
        count += int(num1)

        pos = position + int(movement)  #new position in array
        
        # numbers from -99 to 99 (R)
        if (pos > -100 and pos < 100):
            for i in range(position, pos):
                if i == 0:
                    count += 1
                    break
            position = array[pos]
#------------------------------------------------------------------        
    if condition == "L":    #condition
        pos = position - int(movement)  #new position
        pos_str = str(pos)  #for string manipluation
        
        # numbers from 99 to 999
        if pos > 99 and pos <= 999:
            num1 = pos_str[0]
            pos -= (int(num1)*100)
            
        # numbers greater than 999    
        elif pos > 999:
            num1 = pos_str[0:2]
            pos -= (int(num1)*100)     
        
        # numbers from -999 to -99
        elif pos >= -999 and pos <= -99:
            num1 = pos_str[1]
            pos += (int(num1)*100)

        # numbers less than -999
        elif pos < -999:
            num1 = pos_str[1:3]
            pos += (int(num1)*100)

        #after everything is completly checked
        count += int(num1)

        # numbers from -99 to 99 (L)
        if (pos > -100 and pos < 100):
            for i in range(position, pos, -1):
                if i == 0:
                    count += 1
                    break
            position = array[pos]

print(f"Password: {count}")