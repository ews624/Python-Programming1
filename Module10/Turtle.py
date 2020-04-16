import turtle
from turtle import *

def tree(branchLen,leonardo): 
    if branchLen > 5:
        leonardo.forward(branchLen)
        leonardo.width(leonardo.width()-1)
        leonardo.right(20)
        tree(branchLen-15,leonardo)
        leonardo.left(40)
        tree(branchLen-15,leonardo)
        leonardo.right(20)
        leonardo.backward(branchLen)
        leonardo.width(leonardo.width()+1)

def main():
    leonardo = turtle.Turtle()
    myWin = turtle.Screen()
    leonardo.width(7)
    leonardo.left(90)
    leonardo.up()
    leonardo.backward(100)
    leonardo.down()
    leonardo.color("green")
    tree(75,leonardo)
    turtle.clearscreen()
    level = 3 
    size = 200
    penup() 
    goto(-size / 2.0, size / 2.0) 
    pendown() 
    # For positioning turtle 
    hilbert(level, 90, size/(2**level-1))        
    done()  
    myWin.exitonclick()

def hilbert(level, angle, step): 
  
    # Input Parameters are numeric 
    # Return Value: None 
    if level == 0: 
        return
  
    right(angle) 
    hilbert(level-1, -angle, step) 
  
    forward(step) 
    left(angle) 
    hilbert(level-1, angle, step) 
  
    forward(step) 
    hilbert(level-1, angle, step) 
  
    left(angle) 
    forward(step) 
    hilbert(level-1, -angle, step) 
    right(angle) 

main()



