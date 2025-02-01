def cherryPie():
    portionSize = float(input("what is the length of a portion in cm: "))
    numberofportionWidth = int(input("How many portions fit the width of the tray: "))
    numberofportionLength = int(input("How many portions fit the length of the tray: "))

    length = numberofportionLength * portionSize
    numProtion = numberofportionWidth * numberofportionLength
    cost = ((portionSize ** 2)*1.2)+10
    costoftray = numProtion * cost
    numTrays = int(100000 // costoftray)

    print("The length of the tray is",length,"cm")
    print("The total number of protions on one tray is",numProtion)
    print("the cost of each protion is",cost,"pence")
    print("The number of complete trays of pie that could be made with $100 is ",numTrays)

cherryPie()
