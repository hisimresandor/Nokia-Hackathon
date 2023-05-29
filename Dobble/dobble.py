import os
import random

# Változók létrehozása
n = 0
m = 0
num = 0

# Paraméterek bekérése
while n < 1 or m < 1:
    os.system("cls")
    
    n = int(input("Hány darab szám legyen a kártyán? "))
    m = int(input("Mekkora legyen a pakli? "))

# Első "kártya" létrehozása
pakli = [[random.randrange(1, 100)]]
for i in range(1, n):
    while True:
        num = random.randrange(1, 100)
        if num not in pakli[0]:
            pakli[0].append(num)
            break

# További "kártyák" létrtehozása
for i in range(1, m):
    pakli.append([random.randrange(1, 100)])
    for j in range(1, n):
        while True:
            num = random.randrange(1, 100)
            if num not in pakli[i]:
                pakli[i].append(num)
                break

# Pakli kiíratása
for i in range(len(pakli)):
    for j in range(len(pakli[i])):
        print(pakli[i][j], end=" ")
    print("")