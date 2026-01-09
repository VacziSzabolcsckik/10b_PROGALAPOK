# Jancsi és Juliska autós kártyát gyűjtenek. Hogy ne legyen vita és gyorsan meg tudják különböztetni melyik autó kié, ezért a következőt találták ki. Mivel minden autó végsebessége 3 jegyű, ezért megnézik a középső számot. Ha páros akkor Jancsié, ha páratlan akkor Juliskáé. 
# Van összesen 30 kártyájuk. Szeretik egymás mellé rakni a kártyákat. Szimuláld a feladatot!
# Írj egy programot, ami kigenerál [300, 499] között egy számot úgy, hogy minden páros helyen Jancsi kártyája van, minden páratlan helyen Juliskáé!
# Add meg Jancsi autóinak végsebességének átlagát!
# Add meg hány darab autója van Juliskának, ami 380-nál nagyobb a végsebessége!
import random
import math
"""
autoskartya = []
kartya = random.randint(301,453)
kartyaszam = 0

while kartyaszam != 30:
    kartya = random.randint(301,453)
    kartyaszam += 1
    for index in range(0,30,1):
        if index % 2 == 0 and kartya[1] % 2 == 0:
            autoskartya.append(kartya) 
#print(kartya, end=" ")
print(autoskartya)
"""

"""
    for kozep in kartya:
        if kartya[1] % 2 == 0:
            janautoskartya.append(kartya)
        else:
            julautoskartya.append(kartya)
"""

kartyak = []

for i in range(0,30,1):
    elso = random.randint(1,4)
    masodik = -1
    if(i % 2 == 1): #Jancsi száma
        masodik = random.randint(0,4)*2
    else: #Juliska száma
        masodik = random.randint(0,4)*2+1
    harmadik = random.randint(0,9)
    #szam = int(str(elso)+str(masodik)+str(harmadik))
    szam = elso * 100 + masodik * 10 + harmadik
    kartyak.append(szam)
print(kartyak)

josszeg = 0
db = len(kartyak)/2

for kar in range(1, len(kartyak), 2):
    josszeg += kartyak[kar]
    jatlag = josszeg / db
print(josszeg)
print("Jancsi autóinak végsebességének átlaga: ",round(jatlag, 2))

juliveg = 0

for i in range(0, len(kartyak), 2):
    if kartyak[i] > 380:
        juliveg += 1

print("Juliskának",juliveg,"db autója van ami gyorsabb mint 380 km/h")

