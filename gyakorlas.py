import random

szoveg = input("Írj egy szót!:")
megforditott = ""
for elem in range(-1, -len(szoveg)-1,-1):
    print((szoveg[elem] + " ")*3 , end=" ")
    megforditott += szoveg[elem]
print()

for elem in range(3):
   print(megforditott, end=" ")

osszeg = 0
for index in range(1, 11, 1):
    szam = random.randint(1,9)
    osszeg += szam 
    print(szam, end=" ") 
    print(osszeg)
print()


szoveg = input("Írj egy szót!:")
megforditott = ""
for elem in range(-1,-len(szoveg) - 1, -2):
    print(szoveg[elem], end=" ")


szoveg = input("Adj meg egy szöveget: ")

uj_szoveg = ""
for betu in szoveg:
    if betu != " ":
        uj_szoveg += betu

print(uj_szoveg)

szoveg = input("Szó:")
if szoveg == szoveg[::-1]:
    print("palindrom")
else:
    print("nem palindrom")

szoveg = input("Szó:")
megforditott = ""
for index in szoveg:
    megforditott = index + megforditott

if szoveg == megforditott:
    print("palindrom")
else:
    print("nem palindrom")