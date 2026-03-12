user_input = """R667
R5
R531"""
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
            pos_str = str(movement)  #for string manipluation
            pos = position + int(movement)  #new position in array
            movement = int(movement)
            # numbers from 99 to 999
            if movement > 99 and movement <= 999:
                num1 = pos_str[0]
                movement -= (int(num1)*100)
                
            # numbers greater than 999    
            elif movement > 999:
                num1 = pos_str[0:2]
                movement -= (int(num1)*100)     
            
            # numbers from -999 to -99
            elif movement >= -999 and movement <= -99:
                num1 = pos_str[1]
                movement += (int(num1)*100)

            # numbers less than -999
            elif movement < -999:
                num1 = pos_str[1:3]
                movement += (int(num1)*100)

            #after everything is completly checked
            count += int(num1)
            
            # numbers from -99 to 99 (R)
            if (pos > -100 and pos < 100):
                for i in range(position, pos):
                    if i == 0:
                        count += 1
                        break
                position = array[pos]

            if position == 0:
                count += 1
print(count)