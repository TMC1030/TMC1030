"""
from graphics import *

def clickToClose(win):
    win.getMouse()
    win.close()

win = GraphWin("HELLO",500,500)
win.setBackground("White")

#Rectangle
t1Point = win.getMouse()
brPoint = win.getMouse()
rec = Rectangle(t1Point, brPoint)

rec.draw(win)

#Circle
centre = Point(250,250)
circle1 = Circle(centre,100) #Circle Coordinate
circle1.draw(win)
circle2 = Circle(Point(250,250),75)
circle2.draw(win)
circle3 = Circle(Point(250,250),50)
circle3.draw(win)
circle1.setFill("Blue") #Colour
circle2.setFill("Yellow")
circle3.setFill("Red")

circle2.move(50, 75) #The Circle move to that point
print("circle2's radius =", circle2.getRadius())
print("circle2's centre =", circle2.getCenter())

#Line
line1 = Line(Point(50,25), Point(150,75)) #Original Line
line1.draw(win)

line1.move(0,100)
line1.setWidth(5) #Width the line
line1.setOutline("red") #Colour

#Triangle
triangle = Polygon(Point(100,40),Point(40,100),Point(170,100))
triangle.draw(win)
triangle.setFill("GREY")

#Hexagons
points = [Point(100,30),Point(30,70),Point(30,130),
          Point(100,170),Point(170,130), Point(170,70)]
hexagon = Polygon(points)
hexagon.draw(win)
hexagon.setFill("Blue")

#Text objects
message = Text(Point(250,250),"BONJOUR")
message.draw(win)
message.setSize(30)
message.setFace("times roman")
message.setTextColor("RED")

#Entry objects
inputBox = Entry(Point(200, 200), 10)
inputBox.draw(win)
message = Text(Point(200,100),"Enter your name:")
message.draw(win)
win.getMouse()
userInput = inputBox.getText()
message.setText("Hello,"+userInput)

clickToClose(win) #when type "clickToClose", must add the window name

# String Data Type
string1 = "Hello"
string2 = 'World'
print("Hello World")
print(string1, string2)
type("XXX") #Remark

#Basic string operations
course = 'Computer Science'
studentID = "up1234567"
print(("Welcome to:" + " ") * 4 + course)
print("\n" * 2 + "Your ID number is:\t" + studentID)

# * is repetition
# + is concatenation
# \t is tab
# \n is next line

#Indexing & slicing strings
myString = "Hello World"
print(len(myString)) #Length of the string
print(myString[0]) #The number represents letter of the string
print(myString[-1]) #The number represents letter of the string(Reverse)
print(myString[0:5]) #The first number is the letter start and second one is the one to finish with
print(myString[2:])# X: means retrieving all of the characters of the string
print(myString[:-4])# :X means retrieving all of the characters of the string(Reverse)
print(myString[:])# : means print the whole string

#String Methods
myString = "Hello!"
print(myString.upper())
print(myString.lower())
print(myString.find("lo")) #find is there "X" in the string
print(myString.find("mp")) #find is there "X" in the string. If there isn't any then will be -1
print(myString.count("l")) #Count how many "X" are in the string
print(myString.count("z"))
words = myString.split()
print(words[0])
aString = "a:list:of:words"
print(aString.split(":")) #.split() means split out the whole string
print(myString.split("11"))

#Chaining methods
print("hello".upper().replace("E",'3').replace('O','0')) #replacing X with a new Y
#Character and Number Conversion
print(chr(98)) #expected to enter an integer
print(chr(120)) #returns the character that represents the specified unicode
print(chr(960)) #an integer representing a valid Unicode code point
print(chr(8364))
print(ord("a"))
print(ord("b"))
print(ord("A"))
print(ord("z"))
print(ord("b") - ord("a") + 1)
print(ord("z") - ord("a") + 1)

#String formatting
import math
x = 10.123456789
y = 20
print("the values are {0:0.4f} and {1:8}.".format(x, y))

print("The value {0:0.4f} is pi".format(math.pi))
print("The value {0:0.2f} is pi".format(math.pi))
print("The value {0:8.2f} is pi".format(math.pi))
print("The value {0:<8.2f} is pi".format(math.pi))

name = "Alice"
age = 22
height = 165.65
print("{} is {} years and {:.1f} cm".format(name, age, height))

message = "pi rounded to 3 decimal places:\t{:>10.2f}".format(math.pi)

def main():
    greet("Vicky")
    greet("Tom")
    greet("Fred")
    greet("Sam")
    greet("Gemma")
def greet(name):
    print("Hello " + name + ".", end=" ")
    print("How are you today?")

def square(x):
    return x * x
print(square(2))

z = 3
y = square(z)
print(y)

def sumDiff(n1, n2):
    return n1 + n2, n1 - n2
print(sumDiff(10,3))

main()
"""""
def product(a, b):
    return a * b

def divide(a, b):
    return a / b

def divideAndProduct(a, b):
    productResult = product(a, b)
    divideResult = divide(a, b)
    return productResult, divideResult
