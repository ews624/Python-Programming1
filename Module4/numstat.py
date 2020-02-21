import math

program_run = True
while(program_run):
    while(True):
        try:
            fileName = str(input("Enter the name of the file: "))
            
        except:
            print("Could not open file")
        else:
            break

    try:
        f = open(fileName, "r")
        

    except:
        print("Error reading File")
    else:
        count = 0
        fileSum = 0
        average = 0
        maximum = 0
        minimum = 100000
        fileRange = 0
        for line in f:
            count += 1
            fileSum = fileSum + int(line)
            if(maximum < int(line)):
                maximum = int(line)
            if(minimum > int(line)):
                minimum = int(line)
        average = fileSum / count
        fileRange = maximum - minimum
        print("Sum : ", fileSum)
        print("Count: ",count)
        print("Average: ", average)
        print("Maximum: ", maximum)
        print("Minimum: ", minimum)
        print("Range: ", fileRange)
        another_one= input('Do you want to do another calculation? (y/n): ')
        if(another_one != 'y'):
            program_run = False
        
        
