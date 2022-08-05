'''
DrawRow.py

@author: Georgie Stammer
'''

import turtle, BoundingBox, TurtleShapes

def drawRowsOfRows(turt, func):
    """
    Draws 10 rows of overlapping dusk sky images using the drawDuskSky function
    """
    turt.up()
    y = 250
    size = 15
    for n in range(10):
        turt.goto(-300 + size, y)
        for m in range((300//size) * 2):
            func(turt, size)
            turt.forward(size)
        y -= size
        size += 5


if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()

    t = turtle.Turtle()
    t.speed(0)
    drawRowsOfRows(t, TurtleShapes.drawOneDuskSky)
    
    win.exitonclick()