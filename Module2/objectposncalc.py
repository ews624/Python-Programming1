print('Ethan\'s Object Position Calculator')

program_run = True

while(program_run):
    while(True):
        try:
            pos = float(input('Enter Initial Position in m: '))
            if(pos < 0):
                print('Negative values are not allowed')
                continue
        except ValueError:
            print('The value you entered is invalid. Only numerical values are valid')
        else:
            break

    while(True):
        try:
            velo = float(input('Enter Initial Velocity in m/s: '))
            if(velo < 0):
                print('Negative values are not allowed')
                continue
        except ValueError:
            print('The value you entered is invalid. Only numerical values are valid')
        else:
            break
        
    while(True):
        try:
            accel = float(input('Enter acceleration in m/s^2: '))
            if(accel < 0):
                print('Negative values are not allowed')
                continue
        except ValueError:
            print('The value you entered is invalid. Only numerical values are valid')
        else:
            break
        
    while(True):
        try:
            time = float(input('Enter the amount of time in s: '))
            if(time < 0):
                print('Negative values are not allowed')
                continue
        except ValueError:
            print('The value you entered is invalid. Only numerical values are valid')
        else:
            break
    
    final_pos = pos + (velo * time) + (.5 * accel * time * time)
    print('Final Position is : ', final_pos) 

    another_one= input('Do you want to do another calculation? (y/n): ')
    if(another_one != 'y'):
            program_run = False
