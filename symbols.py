# SYMBOL GENERATION

from turtle import *

def main():
    colors=["red","orange","green","blue","seagreen","royalblue"]
    reset()
    Screen()
    up()
    goto(-320,-195)
    width(90)
    for pcolor in colors:
        color(pcolor)
        down()
        forward(640)
        up()
        backward(640)
        left(90)
        forward(66)
        right(90)

    width(55)
    color("white")
    goto(0,-170)
    down()

    circle(170)
    left(90)
    forward(340)
    up()
    left(180)
    forward(170)
    right(45)
    down()
    forward(170)
    up()
    backward(170)
    left(90)
    down()
    forward(170)
    up()
    goto(0,300)


main()

    

    
    
       
    
    
    
        
    
    
