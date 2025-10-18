import random

# lebegőpontos - float - tört
a = 1.25
b = float(input("adjon meg egy tizedes törtet: "))
print(b*4)

# generáljon ki [1,10[ közötti tört számot 2 tizedesjegyre
# pl. 1.36, 2.30

# c = float(random.randint(100,999)/100)
c = random.random() # [0,1[
print(round(c,2))
# HF befejezni

# Szövegkezelés
szoveg = input("adjon meg egy szöveget: ")
print(szoveg)
print("szoveg hossza: ",len(szoveg))
print("első karakter",szoveg[0])
# szöveg karakterekből épül fel
# szöveg = karakter lánc
karakter = szoveg[0]
kod = ord(szoveg[0])
print(kod)
ujkod = kod + 1
ujkarakter = chr(ujkod)
print(ujkarakter)

d = chr(random.randint(97,122))
e = chr(random.randint(97,122))
f = chr(random.randint(97,122))
print(d,e,f)

# kérje be a felhasználó keresztnevét! Generáljon neki egy jelszót az első 3 karakterének ASCII kódjának szorzatát! Ha nincs a név 3 jegyű, akkor kettő esetén a hossz érték legyen a szorzat 3. tagja 1 esetén pedig a szám köbe legyen
# Alma - 65 * 108 * 109
# Co - 67 * 111 * 2
# G - 71 * 71 * 71

keresztnev = input("Add meg a keresztneved: ")

if len(keresztnev) == 0:
    print("Nincs név")

if len(keresztnev) >= 3:
        szorzat = ord(keresztnev[0]) * ord(keresztnev[1]) * ord(keresztnev[2])
elif len(keresztnev) == 2:
        szorzat = ord(keresztnev[0]) * ord(keresztnev[1]) * len(keresztnev)
else:
        szorzat = ord(keresztnev[0]) ** 3

print("A generált jelszavad: " + str(szorzat))
