import random as r

"""
Elől tesztelős ciklus
while ciklus

- Nem tudjuk, hogy hányszor fog lefutni (hányszor ismétel)
- Feltételhez kötött!
- Akkor ismétel, ha feltétel igaz

while(Feltétel):
    utasítások (szekvencia)
"""

# Generáljon véletlen számokat [0,10] között, amíg nullát nem kapunk!

velszam = r.randint(0,10)
print(velszam)
while(velszam != 0):
    velszam = r.randint(0,10)
    print(velszam, end=" ")
print()

# kérjen be számokat, addig amíg nullát nem adnak meg!

szam = input("Írj egy számot(0-nál kilép): ")
osszeg = 0
db = 0
while(int(szam) != 0):
    print(szam, end="\n")
    szam = input("Írj egy számot(0-nál kilép): ")
print(osszeg/db)
print()

while(szam != 0)
    osszeg += szam
    db += 1
    szam = int(input("írj egy számot(0-nál kilép): "))
print(round(osszeg/db,2))

#Adott egy szöveg. Adja meg, hogy van-e benne x betű!

szoveg = "Ebben a szövegben nincs x"