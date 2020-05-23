from turtle import *
import turtle

def check_input():
    while True:
        try:
            depth = int(input("How much depth do you want?"))
            if depth <1 or depth >6:
                print("Please choose a number between 1 and 6")
        except:
            print("Please choose a number between 1 and 6")
        if depth >= 1 and depth <= 6:
            return depth

        
    return depth

def sierpinski(length, depth):
    if depth > 1: dot()
    if depth == 0:
        stamp()
    else:
        
        forward(length)
        sierpinski(length/2, depth-1)
        backward(length)
        left(120)
        
        forward(length)
        sierpinski(length/2, depth-1)
        backward(length)
        left(120)
        
        forward(length)
        sierpinski(length/2, depth-1)
        backward(length)
        left(120)

def main():
    print("Ethan's Sierpinski Triangle! Choose how big you want it!")
    depth =check_input()
    length = depth *(100/3)   
    sierpinski(length,depth)

main()
