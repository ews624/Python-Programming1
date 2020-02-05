print('Ethan\'s Object Position Calculator')
pos = float(input('Enter Initial Position in m: '))
velo = float(input('Enter Initial Velocity in m/s: '))
accel = float(input('Enter acceleration in m/s^2: '))
time = float(input('Enter the amount of time in s: '))

final_pos = pos + (velo * time) + (.5 * accel * time * time)
print('Final Position is : ', final_pos) 
