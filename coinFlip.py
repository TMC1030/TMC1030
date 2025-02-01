from random import random

def getInputs():
    return int(input("How many times would you like to flip a coin?"))

def simulateFlips(flipAmount):
    headsAmount = 0
    tailsAmount = 0

    for x in range(flipAmount):
        randomNum = random()
        if randomNum < 0.5:
            headsAmount += 1
        else:
            tailsAmount += 1

    headsPropertion = headsAmount / flipAmount
    tailsPropertion = tailsAmount / flipAmount
    return  headsPropertion,tailsPropertion

def displayResults(headsPropertion,tailsPropertion):
    print(f"Heads{headsPropertion},Tail{tailsPropertion}")

def main():
    flipAmount = getInputs()
    result = simulateFlips(flipAmount)
    displayResults(result[0],result[1])

main()
