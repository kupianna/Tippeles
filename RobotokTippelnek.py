import random

def HaromRobotEgyszer():
    szam= random.randint(1,10)

    robot1 = random.randint(1, 10)
    robot2 = random.randint(1, 10)
    robot3 = random.randint(1, 10)

    #debug
    # szam = 2
    # robot1 = 4
    # robot2 = 4
    # robot3 = 4
    # debug vége
    nyertes = ""
    szamlalo = 0
    if robot1 == szam:
       nyertes += " 1. robot "
       szamlalo += 1
    if robot2 == szam:
       nyertes += " 2. robot "
       szamlalo += 1
    if robot3 == szam:
        nyertes += " 3. robot "
        szamlalo += 1
    if szamlalo == 0:
        print("Nem volt találat!")
    elif szamlalo < 3:
        print("eltalálták: ", nyertes)
    else:
        print("Mindenki eltalálta!")


    print (f"Eltalálták: {nyertes}, a szám pedig {szam}")

def EgyRobotHaromszor():
    szam = random.randint(1,10)
    talalat = 0
    tipp = random.randint(1,10)


    if tipp == szam:
        talalat += " Elsőre eltalálta!"
    else:
        tipp = random.randint(1,10)
        if tipp == szam:
            talalat += " Másodikra eltalálta!"
            print(f"Az eredmény: {talalat}")
    # kiíró logika csak egyszer!
    # csinalni utolso else nelkul!

def SokTipp():
    szam = random.randint(1,10)
    tipp = random.randint(1, 10)
    tippDb = 0
    while tippDb < 50 and tipp != szam:
        tippDb += 1
        tipp = random.randint(1, 10)
        if tipp == szam:
            print (f"találat a(z) {tippDb}, tipp")

def CsillagTipp():

    i =0
    be = ""
    osszeg = 0
    paratlanDb = 0
    while be != "*":
        be=input("egész: ")
    if be != "*":
        szam = int(be)
        osszeg += szam
        if szam % 2 ==1:
            paratlanDb +=1

    print (f"összeg: {osszeg}")
    print (f" páratlanok száma: {paratlanDb} ")









