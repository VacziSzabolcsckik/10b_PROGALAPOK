import random as r

# generáljon ki 10 db egy jegyű véletlen számot!
# írassa ki a számok összegét!

osszeg = 0
for a in range(1,11,1):
    velSzam = r.randint(1,9)
    osszeg += velSzam
    print(velSzam, end=" ")
print()
print("Összeg",osszeg)

#Hány db páros véletlen számot generált ki?
# Melyik a legnagyobb véletlen szám