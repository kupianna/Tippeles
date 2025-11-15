import random

def szamgeneralas():
    szam= random.randint(1,10)

    robot1 = random.randint(1, 10)
    robot2 = random.randint(1, 10)
    robot3 = random.randint(1, 10)
    nyertes=0
    if robot1 == szam:
       nyertes += "1. robot"
    if robot2 == szam:
       nyertes += "2. robot"
    if robot3 == szam:
        nyertes += "3. robot"
    if robot1 and robot2 and robot3 ==szam:
       nyertes = robot3
    if robot1 and robot2 ==szam and robot3!=szam:

    if robot1 and robot2 == szam and robot3 !=szam:


    else:
        print ("A harmadik robot találta el!")

