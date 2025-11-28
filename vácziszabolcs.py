import random as r
import math

#1. feladat
print("1. Feladat")
szam = r.randint(10,99)
print(szam)

kszam = "0"
for bszam in range(0, szam, 1):
    bszam = r.randint(100,999)
    hszam = bszam
    print(bszam, end=" ")
    nszam = hszam % 3 == 0
    if nszam == True:
        kszam = int(kszam) + 1
        
print()
print(kszam,"darab hárommal osztható szám van.")
print()

# 2. feladat
print("2. feladat")
szoveg = input("Írj egy szöveget: ")
#for kozepso in range(len(szoveg), len(szoveg), 1):
    #print(szoveg[kozepso], end=" ")
#print()
for paros in range(0, len(szoveg), 2):
    print(szoveg[paros], end="$")
