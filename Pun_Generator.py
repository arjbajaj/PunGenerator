pun1 = ("""What does a house wear?
A DRESS!!!!!!!!!""")
pun2 = ("""Why couldn't the bicyle stand up on it's own?
IT WAS TOO TIRED!!!!!""")
pun3 = ("""	Did you hear about the guy whose whole left side was cut off?
HE'S ALL RIGHT NOW!!!!""")
pun4 = ("""I'd tell you a chemistry joke but I know I wouldn't get a reaction.""")
pun5 = ("""Why don't some couples go to the gym? Because some relationships don't work out.""")
pun6 = ("What kind of shorts do clouds wear? THUNDERWEAR!!")
pun7 = ("What do you call an alligator in a vest? AN INVESTIGATOR!!!")
pun8 = ("How do you organise a space party? YOU PLANET!!!")
pun9 = ("Why do bananas need sunscreen? BECAUSE THEY PEEL!!!")
pun10 = ("RIP boiled water. You will be mist.")
while True:
    vPun = int(input("Input pun number (1-10)"))
    if vPun == 1:
        print(pun1)
    if vPun == 2:
        print(pun2)
    if vPun == 3:
        print(pun3)
    if vPun == 4:
        print(pun4)
    if vPun == 5:
        print(pun5)
    if vPun == 6:
        print(pun6)
    if vPun == 7:
        print(pun7)
    if vPun == 8:
        print(pun8)
    if vPun == 9:
        print(pun9)
    if vPun == 10:
        print(pun10)
    inputPun = input("Do you want to add a pun (Y/N)?")
    if inputPun == "Y":
        inputPunNum = int(input("Choose which pun would you like to change (1-10)"))
        if inputPunNum == 1:
            pun1 = input("You are now changing Pun 1. Input desired Pun")
        if inputPunNum == 2:
            pun2 = input("You are now changing Pun 2. Input desired Pun")
        if inputPunNum == 3:
            pun3 = input("You are now changing Pun 3. Input desired Pun")
        if inputPunNum == 4:
            pun4 = input("You are now changing Pun 4. Input desired Pun")
        if inputPunNum == 5:
            pun5 = input("You are now changing Pun 5. Input desired Pun")
        if inputPunNum == 6:
            pun6 = input("You are now changing Pun 6. Input desired Pun")
        if inputPunNum == 7:
            pun7 = input("You are now changing Pun 7. Input desired Pun")
        if inputPunNum == 8:
            pun8 = input("You are now changing Pun 8. Input desired Pun")
        if inputPunNum == 9:
            pun9 = input("You are now changing Pun 9. Input desired Pun")
        if inputPunNum == 10:
            pun10 = input("You are now changing Pun 10. Input desired Pun")
