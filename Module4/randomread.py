

try:
    f = open("randomnum.txt", "r")
    count = 0
    for line in f:
            print(line)
            count += 1    
    print("Random number count: ", count)
    f.close()

except:
    print("Error Opening file")

    
