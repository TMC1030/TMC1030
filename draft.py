from graphics import *

def clickToClose(win):
    win.getMouse()
    win.close()

def drawSecondToLastNumberPatch(win,tlx,tly,colour):
    for i in range(20,81,20):
            circle = Circle(Point(tlx, tly), 10)
            circle.setFill(colour)
            circle.draw(win)

def twoTriangleDownwards(win,x1,y1,x2,y2,x3,y3,colour):
    triangle = Polygon(Point(x1,y1),Point(x2,y2),Point(x3,y3))
    triangle.setFill(colour)
    triangle2 = Polygon(Point(x1,y1+10), Point(x2,y2+10), Point(x3,y3+10))
    triangle2.setFill(colour)
    triangle.draw(win)
    triangle2.draw(win)

def twoTrianglesRightwards(win,x1,y1,x2,y2,x3,y3,colour):
    triangleRightWards = Polygon(Point(x1,y1),Point(x2,y2),Point(x3,y3))
    triangleRightWards.setFill(colour)
    triangleRightWards2 = Polygon(Point(x1+10, y1), Point(x2+10, y2), Point(x3+10, y3))
    triangleRightWards2.setFill(colour)
    triangleRightWards.draw(win)
    triangleRightWards2.draw(win)

def drawPatch(tlx,tly,colour):

    win = GraphWin("",200,200)

    for y in range(0,100,20):
        for x in range(0,100,20):

            if x % 40 == 0 and y % 40 == 0:
                twoTriangleDownwards(win, x+tlx, y+tly, (x+tlx) + 20, y+tly, (x+tlx) + 10, (y+tly) + 10, colour)
            elif (y + 20) % 40 == 0 and (x+20) % 40 == 0:
                twoTrianglesRightwards(win,x+tlx,y+tly,(x+tlx)+10,(y+tly)+10,(x+tlx),(y+tly)+20,colour)
            else:
                circle = Circle(Point((x+tlx) + 10, (y+tly) + 10), 10)
                circle.setFill(colour)
                circle.draw(win)


    clickToClose(win)

drawPatch(100,100,"red")



"""
    drawRectangle(win,0,0,"blue")
    drawRectangle(win,0,100,"blue")
    drawPatch(win, 0, 200, "blue")
    drawPatch(win,0,300,"blue")
    drawPatch(win,0,400,"orange")
    drawRectangle(win,100,0,"blue")
    drawRectangle(win,100,100,"blue")
    drawPatch(win,100,200,"blue")
    drawPatch(win,100,400,"red")
    drawRectangle(win, 200, 0, "blue")
    drawRectangle(win, 200, 100, "blue")
    drawPatch(win, 200, 200, "orange")
    drawPatch(win, 200, 300, "red")
    drawPatch(win, 200, 400, "red")
    drawRectangle(win, 300, 0, "blue")
    drawRectangle(win, 300, 100, "orange")
    drawRectangle(win,300,200,"red")
    drawRectangle(win,300,300,"red")
    drawRectangle(win,300,400,"red")
    drawRectangle(win,400,0,"orange")
    drawRectangle(win,400,100,"red")
    drawRectangle(win,400,200,"red")
    drawRectangle(win,400,300,"red")
    drawRectangle(win, 400, 400, "red")

def graphSizeSelector():
    graphsize = [5,7,9]

    while True:
        number = int(input("Enter a number between 5,7,9:\n"))

        if number in graphsize:
            screen = number*100
            return screen
            break

        else:
            print("Enter a valid number between 5,7,9!")
            
                if y % 40 == 0:
                twoTrianglesRightwards(win,x,y,x+10,y+10,x,y+20,colour)
            else:
                circle = Circle(Point(x + 10, y + 10), 10)
                circle.setFill(colour)
                circle.draw(win)
                
    crossLine = Line(Point(blx,bly),Point(trx,try))
    
    if x < 500:
        print("Blue")
    elif y > 500:
        print("Orange")
    else:
        print("red")
            
    for r in range(0, 500, 100):
        for c in range(0, 500, 100):
            if r >= 200 and c <= 200:
                if r == 300 and c == 100:
                # P
                else:
                # F
            else:
            # rect
                # Fs and 1P
"""
