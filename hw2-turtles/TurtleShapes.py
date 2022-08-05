'''
TurtleShapes.py

@author: Georgie Stammer
'''

import turtle, BoundingBox

def drawOneShape(turt, size):
    """
    Draws a purple triangle w/ side length size
    """
    turt.shape("turtle")
    turt.color("#7353BA")
    turt.fillcolor("#7353BA")
    turt.begin_fill()
    for n in range(3):
        turt.forward(size)
        turt.left(120)
    turt.end_fill()

def drawOneDuskSky(turt, size):
    """
    Draws a square picture of a dusk sky with a moon (with 4 colors)
    """
    turt.shape("turtle")
    turt.color("#0F1020")
    turt.fillcolor("#0F1020")
    turt.begin_fill()
    turt.right(180)
    for n in range(2):
        turt.forward(size)
        turt.left(90)
        turt.forward(size * 0.5)
        turt.left(90)
    turt.end_fill()
    turt.left(90)
    turt.forward(size * 0.5)
    turt.right(90)
    turt.color("#2F195F")
    turt.fillcolor("#2F195F")
    turt.begin_fill()
    for n in range(2):
        turt.forward(size)
        turt.left(90)
        turt.forward(size * 0.3)
        turt.left(90)
    turt.end_fill()
    turt.left(90)
    turt.forward(size * 0.3)
    turt.right(90)
    turt.color("#7353BA")
    turt.fillcolor("#7353BA")
    turt.begin_fill()
    for n in range(2):
        turt.forward(size)
        turt.left(90)
        turt.forward(size * 0.2)
        turt.left(90)
    turt.end_fill()
    turt.up()
    turt.forward(size * 0.5)
    turt.right(90)
    turt.forward(size * 0.5)
    turt.color("#FAA6FF")
    turt.fillcolor("#FAA6FF")
    turt.begin_fill()
    turt.circle(size * 0.2)
    turt.end_fill()
    turt.color("#0F1020")
    turt.fillcolor("#0F1020")
    turt.begin_fill()
    turt.circle(size * 0.15)
    turt.end_fill()
    turt.forward(size * 0.3)
    turt.right(90)
    turt.forward(size * 0.5)

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()

    t = turtle.Turtle()
    size = 50
    drawOneShape(t, size)
    size = 200
    drawOneDuskSky(t, size)

    win.exitonclick()
