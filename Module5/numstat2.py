import math
from collections import Counter

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
        median = 0
        medList = []
        mode = 0
        for line in f:
            medList.append(int(line))
            count += 1
            fileSum = fileSum + int(line)
            if(maximum < int(line)):
                maximum = int(line)
            if(minimum > int(line)):
                minimum = int(line)
        data = Counter(medList)
        get_mode = dict(data)
        mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

        if len(mode) == count:
            get_mode = "No mode found"
        else:
            get_mode = "[" + ", ".join(map(str, mode)) + "]"
        medList.sort()
        if count % 2 == 0:
            median1 = medList[count//2]
            median2 = medList[count//2 -1]
            median = (median1 + median2)/2
        else:
            median = medList[n//2]
        average = fileSum / count
        fileRange = maximum - minimum
        print("Sum : ", fileSum)
        print("Count: ",count)
        print("Average: ", average)
        print("Maximum: ", maximum)
        print("Minimum: ", minimum)
        print("Range: ", fileRange)
        print("Median: ",median)
        print("Mode: ", get_mode)
        another_one= input('Do you want to do another calculation? (y/n): ')
        if(another_one != 'y'):
            program_run = False
        
        
