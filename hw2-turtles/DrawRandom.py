'''
DrawRandom.py

@author: Georgie Stammer
'''

import turtle, BoundingBox, random, TurtleShapes

def drawEverywhere(turt, func):
    """
    Draws the specified picture from TurtleShapes in random coordinates with
    random sizes with the amount given by an input
    """
    stop = int(input("How many items would you like to draw?"))
    for x in range(0, stop):
        turt.up()
        size = random.randint(20, 100)
        x = random.randint(-250, 250)
        y = random.randint(-200, 200)
        turt.goto(x, y)
        turt.down()
        func(turt, size)
    turt.up()

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()

    t = turtle.Turtle()
    funcNumber = input("Input 0 for drawOneShape, 1 for drawOneDuskSky")
    if funcNumber == "0":
        drawEverywhere(t, TurtleShapes.drawOneShape)
    if funcNumber == "1":
        drawEverywhere(t, TurtleShapes.drawOneDuskSky)
    
    win.exitonclick()