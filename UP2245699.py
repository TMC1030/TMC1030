from graphics import *

def clickToClose(win):
    win.getMouse()
    win.close()

def main():
    graphsize = [5,7,9]
    valid_colours = ['red','green','blue','magenta','orange','yellow','cyan']
    colours = []

    number = int(input("Enter a number between 5,7,9: "))

    while len(colours) < 3:
        colour = str(input("Choose 3 colours(red, green, blue, magenta, orange, yellow, cyan): "))
        if colour in valid_colours and colour not in  colours:
            colours.append(colour)
        else:
            print("Invalid colour. Please enter the colour name that are provided on the list.")

        print("Colors entered:",colours ,"\n")

    if number == graphsize[0]:
        print(fiveByFive(colours))
    elif number == graphsize[1]:
        print(sevenBySeven(colours))
    elif number == graphsize[2]:
        print(nineByNine(colours))
    else:
        print("Invalid size. The valid sizes are 5,7,9")
def drawPatch(win,tlx,tly,colours):
    for i in range(20, 81, 20):
        verticalLine = Line(Point(i+tlx, 0+tly), Point(i+tlx, 100+tly))
        verticalLine.setFill(colours)
        verticalLine.draw(win)

        horizontalLine = Line(Point(0+tlx, i+tly), Point(100+tlx, i+tly))
        horizontalLine.setFill(colours)
        horizontalLine.draw(win)

        for i in range(10, 91, 20):
            for j in range(10, 91, 20):
                text = Text(Point(i+tlx, j+tly), "hi!")
                text.setSize(8)
                text.setFill(colours)
                text.draw(win)

def drawPatch2(win,tlx,tly,colour):
    for y in range(0,100,20):
        for x in range(0,100,20):

            if x % 40 == 0 and y % 40 == 0:
                twoTriangleDownwards(win, x+tlx, y+tly, (x+tlx) + 20, y+tly, (x+tlx) + 10, (y+tly) + 10, colour)
            elif (y + 20) % 40 == 0 and (x+20) % 40 == 0:
                twoTrianglesRightwards(win,x+tlx,y+tly,(x+tlx)+10,(y+tly)+10,(x+tlx),(y+tly)+20,colour)
            else:
                circle = Circle(Point((x+tlx) + 10, (y+tly) + 10), 10)
                circle.setFill(colour)
                circle.setOutline(colour)
                circle.draw(win)

def drawSecondToLastNumberPatch(win,tlx,tly,colour):
    for i in range(20,81,20):
            circle = Circle(Point(tlx, tly), 10)
            circle.setFill(colour)
            circle.draw(win)

def twoTriangleDownwards(win,x1,y1,x2,y2,x3,y3,colour):
    triangle = Polygon(Point(x1,y1),Point(x2,y2),Point(x3,y3))
    triangle.setFill(colour)
    triangle.setOutline(colour)
    triangle2 = Polygon(Point(x1,y1+10), Point(x2,y2+10), Point(x3,y3+10))
    triangle2.setFill(colour)
    triangle2.setOutline(colour)
    triangle.draw(win)
    triangle2.draw(win)

def twoTrianglesRightwards(win,x1,y1,x2,y2,x3,y3,colour):
    triangleRightWards = Polygon(Point(x1,y1),Point(x2,y2),Point(x3,y3))
    triangleRightWards.setFill(colour)
    triangleRightWards.setOutline(colour)
    triangleRightWards2 = Polygon(Point(x1+10, y1), Point(x2+10, y2), Point(x3+10, y3))
    triangleRightWards2.setFill(colour)
    triangleRightWards2.setOutline(colour)
    triangleRightWards.draw(win)
    triangleRightWards2.draw(win)

def drawRectangle(win,x,y,colour):
    rectangele = Rectangle(Point(0+x,0+y),Point(100+x,100+y))
    rectangele.setFill(colour)
    rectangele.setOutline(colour)
    rectangele.draw(win)

def fiveByFive(colours):

    win = GraphWin("5x5",500,500)
    win.setBackground("white")

    drawPatch(win, 0, 400,colours[1])
    drawPatch2(win,100,300,colours[1])
    drawPatch(win, 200, 200, colours[1])
    drawRectangle(win, 300, 100, colours[1])
    drawRectangle(win, 400, 0, colours[1])

    for a in range(200,400,100):
        drawPatch(win,0,a,colours[0])
        drawPatch(win,100,200,colours[0])
    for b in range(300,500,100):
        drawPatch(win,200,b,colours[2])
        drawPatch(win, 100, 400, colours[2])
    for x in range(0,400,100):
        drawRectangle(win,0+x,0,colours[0])
        drawRectangle(win, 400, 100 + x, colours[2])
    for y in range(0,300,100):
        drawRectangle(win,0+y,100,colours[0])
        drawRectangle(win,300,200+y,colours[2])

    clickToClose(win)

def sevenBySeven(colours):

    win = GraphWin("7x7", 700,700)
    win.setBackground("white")

    drawPatch2(win, 100, 400, colours[0])
    drawPatch2(win, 100, 500, colours[1])
    drawPatch2(win, 200, 400, colours[1])
    drawPatch2(win, 200, 500, colours[2])

    drawPatch(win, 0, 600, colours[1])
    drawPatch(win, 300, 300, colours[1])
    drawRectangle(win, 400, 200, colours[1])
    drawRectangle(win, 500, 100, colours[1])
    drawRectangle(win,600,0,colours[1])

    for x in range(0, 600, 100):
        drawRectangle(win, 0 + x, 0, colours[0])
        drawRectangle(win, 600, 100 + x, colours[2])

    for y in range(0, 500, 100):
        drawRectangle(win, 0 + y, 100, colours[0])
        drawRectangle(win, 500, 200 + y, colours[2])

    for z in range(0,400,100):
        drawRectangle(win,0+z,200,colours[0])
        drawRectangle(win,400,300+z,colours[2])

    for aa in range(0,300,100):
        drawPatch(win,0+aa,300,colours[0])
        drawPatch(win,300,400+aa,colours[2])

    for ab in range(0,200,100):
        drawPatch(win,0,400+ab,colours[0])
        drawPatch(win,100+ab,600,colours[2])

    clickToClose(win)

def nineByNine(colours):

    win = GraphWin("9x9", 900, 900)
    win.setBackground("white")

    drawPatch2(win, 100, 500, colours[0])
    drawPatch2(win, 100, 600, colours[0])
    drawPatch2(win, 100, 700, colours[1])
    drawPatch2(win, 200, 500, colours[0])
    drawPatch2(win, 200, 600, colours[1])
    drawPatch2(win, 200, 700, colours[2])
    drawPatch2(win, 300, 500, colours[1])
    drawPatch2(win, 300, 600, colours[2])
    drawPatch2(win, 300, 700, colours[2])

    drawPatch(win, 0, 800, colours[1])
    drawPatch(win, 400, 400, colours[1])

    drawRectangle(win, 500, 300, colours[1])
    drawRectangle(win, 600, 200, colours[1])
    drawRectangle(win, 700, 100, colours[1])
    drawRectangle(win, 800, 0, colours[1])

    for x in range(0, 800, 100):
        drawRectangle(win, 0 + x, 0, colours[0])
        drawRectangle(win, 800, 100 + x, colours[2])

    for y in range(0, 700, 100):
        drawRectangle(win, 0 + y, 100, colours[0])
        drawRectangle(win, 700, 200 + y, colours[2])

    for z in range(0,600,100):
        drawRectangle(win,0+z,200,colours[0])
        drawRectangle(win,600,300+z,colours[2])

    for aa in range(0,500,100):
        drawRectangle(win,0+aa,300,colours[0])
        drawRectangle(win,500,400+aa,colours[2])

    for ab in range(0,400,100):
        drawPatch(win,0+ab,400,colours[0])
        drawPatch(win,0,400+ab,colours[0])
        drawPatch(win,400,500+ab,colours[2])
        drawPatch(win,100+ab,800,colours[2])

    clickToClose(win)

main()