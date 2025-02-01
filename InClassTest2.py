from graphics import *

def clickToClose(win):
    win.getMouse()
    win.close()

def drawCircle(win,centre,radius,colour):
    circle = Circle(centre,radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

def drawCircles():
    win = GraphWin("Circles",600,600)
    radius = 30

    for x in range(15):
        clickedPoint = win.getMouse()
        x = clickedPoint.getX()
        y = clickedPoint.getY()

        if x < 300 and y < 300:
            circle = Circle(clickedPoint,radius)
            circle.setOutline("Blue")
            circle.draw(win)
        elif x >= 300 and y < 300:
            circle = Circle(clickedPoint, radius)
            circle.setFill("Blue")
            circle.draw(win)
        elif x < 300 and y >= 300:
            circle = Circle(clickedPoint, radius)
            circle.setOutline("Pink")
            circle.draw(win)
        else:
            circle = Circle(clickedPoint, radius)
            circle.setFill("Pink")
            circle.draw(win)

#drawCircles()

def drawCircles2():
    win = GraphWin("Circles 2",600,600)
    radius = 30

    def colourSelector():
        colour = ["Blue","Pink"]

    for _ in range(10, 3 * radius * 2):
        for columns in range(10, 3 * radius, radius):
            point = win.getMouse()
            x = point.getX()
            y = point.getY()
            colour = colourSelector(x, y, radius, radius)
            drawCircles(win, columns, _,radius, colour)

drawCircles2()