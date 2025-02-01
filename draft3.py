def getName():
    name = input("Enter your name:")
    while name.isalpha() == False:
        name = input("Enter your name:")

    print(f"Your name is {name}")

getName()