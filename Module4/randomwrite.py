import math
import random


count_randomNumbers = int(input('How many random numbers do you want?'))
low_range = int(input('What is the lowest the random number should be: '))
high_range = int(input('What is the highest the random number should be: '))
        
try:
      f = open("randomnum.txt", "x")
      for x in range(count_randomNumbers):
          randomNum = str(random.randrange(low_range, high_range+1,2))
          f.write(randomNum+ '\n')
          print(randomNum)
      f.close()
except FileExistsError:
      f = open("randomnum.txt", "w")
      for x in range(count_randomNumbers):
          randomNum = str(random.randrange(low_range, high_range+1,2))
          f.write(randomNum + '\n')
          print(randomNum)
      f.close()
print('The random numbers were written to randomnum.txt')

