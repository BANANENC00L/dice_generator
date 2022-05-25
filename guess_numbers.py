import random

v = 0
a = random.randint(1,100)
while True:
    print("Rate meine Zahl!")
    b = input()
    b = int(b)
    if a == b:
        print("Glückwunsch! Deine Zahl ist richtig!")
        break

    if b > a:
        print("Meine Zahl ist kleiner! Du kek!")
        v = v + 1
        print("Versuch:",v)

    if b < a:
        print("Meine Zahl ist größer! Du kek!")
        v = v + 1
        print("Versuch:",v)