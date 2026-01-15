import math
import random

szovegbetu = ""
print("1. Feladat")
#1. feladat
szoveg = input("Írjon egy szöveget: ")
for i in range(0,len(szoveg),1):
    print(szoveg[i],end="")
    
print()
hanyadik = input("Adja meg hányadik karakterig írjam a szöveget: (1 és szöveghossz között!): ")

for i in range(0,int(hanyadik),1):
    print(szoveg[i], end="")
print()
print("2. Feladat")
#2. feladat

osszeg = 0
db = 0
dbp = 0
while db < 13:
    szam = random.randint(10,99)
    if szam % 3 == 0:
        szam = random.randint(10,99)
    else:
        print(szam, end=" ")
        db += 1
    
    if szam % 2 == 0:
        szam = random.randint(10,99)
    else:
        osszeg += szam
        dbp += 1
    #osszeg += szam

print()
print()

atlag = osszeg / dbp
print("Páratlanok összege: ",osszeg)
print("Páratlanok darabszáma: ", dbp)
print("Páratlan számok átlaga: ", round(atlag,1))