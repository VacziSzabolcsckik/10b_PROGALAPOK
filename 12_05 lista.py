import random

#a szövegben van-e sz betű
szoveg = "palap"
dube = "cs" #duplabetu
print(szoveg)
"""
if "sz" in szoveg:
    print("benne van az sz betű")
else:
    print("nincs benne sz betű")
"""
index = 0
while(index < len(szoveg)-1 and not(szoveg[index] == dube[0] and szoveg[index+1] == dube[1])):
    index+=1
if(szoveg[index] == dube[0] and szoveg[index+1] == dube[1]):
    print("Van benne ",dube ,"betű")
else:
    print("Nincs benne ",dube,"betű")
"""
if(index<len(szoveg)):
    print("benne van az sz betű")
else:
    print("nincsen benne az sz betű")
"""

# palindrom-e
ujszoveg = ""

for index in range(len(szoveg)-1, -1, -1):
    ujszoveg += szoveg[index]
if(ujszoveg == szoveg):
    print("A szöveg palindrom")
else:
    print("A szöveg nem palindrom")

j = 0
while(j<len(szoveg)/2 and szoveg[j] == szoveg[len(szoveg)-1-j]):
    j+=1
if(j<len(szoveg)/2):
    print("A szöveg nem palindrom")
else:
    print("A szöveg palindrom")

"""
lista - dinamikus
- tudunk bele új elemet rakni, ezzel nő az elemszáma
- tudunk belőle törölni, ezzel csökken az elemszáma
- lekérhető bármelyik eleme
- módosítható bármelyik elem
deklarálás + inicializálás:
létrehozás + kezdőérték adás:
lista_neve = []
új elem hozzáadása:
lista_neve.append(ujelem)
elem törlése:
lista_neve.remove(elem)
beégetett lista:
lista_neve = [3,2,5,7,1]
lista hossza:
len(lista_neve)
"""

szamok = [3,2,5,7,1]
print(szamok)
szamok.append(12)
print(szamok)
szamok.remove(3)
print(szamok)
print("Első elem:",szamok[0])
print("Utolsó elem:", szamok[len(szamok)-1])
#print("Utolsó elem:",szamok[-1])
print("Lista hossza:",len(szamok))

#házi feladat
#tölts fel egy 13 elemű listát
#számok átlaga
#hány darab páros szám van a listában
#van-e benne nulla