from graphics import *

def clickToClose(win):
    win.getMouse()
    win.close()

def drawStickFigure():
    win = GraphWin("Stick figure", 300, 200)
    win.setBackground("White")
    head = Circle(Point(200, 60), 20)
    head.draw(win)
    body = Line(Point(200, 80), Point(200, 120))
    body.draw(win)
    arm1 = Line(Point(200, 90), Point(160, 80))
    arm1.draw(win)
    arm2 = Line(Point(200, 90), Point(240, 80))
    arm2.draw(win)
    leg1 = Line(Point(200, 120), Point(170, 170))
    leg1.draw(win)
    leg2 = Line(Point(200, 120), Point(230, 170))
    leg2.draw(win)

    leftEye = Circle(Point(190,55),5)
    leftEye.draw(win)
    leftEye2 = Line(Point(185,55),Point(195,55))
    leftEye2.draw(win)

    rightEye = Circle(Point(210,55),5)
    rightEye.draw(win)
    leftEye2 = Line(Point(205, 55), Point(215, 55))
    leftEye2.draw(win)

    duvet = Rectangle(Point(160,80),Point(240,170))
    duvet.setFill("orange")
    duvet.draw(win)

    win.getMouse()
    text = Text(Point(150,55),"Buz")
    text.draw(win)

    text = "Buz"

    for _ in range(5):
        win.getMouse()
        text2 = text + "z"
        text2 = Text(Point(162,55),"z")
        text2.draw(win)





    clickToClose(win)

drawStickFigure()