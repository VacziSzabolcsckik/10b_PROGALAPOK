"""
utasítás (szekvencia)
 - menj előre
 - fordulj
 - szívd be a levegőt
 - fújd ki a levegőt
 - ...
 - írasd ki - print()
 - tárold el - változónév = érték
 - számold ki - változónév = <Képlet>
 - kérd be - input("add meg: ")

Elágazás - (szelekció)
 - ha piros a lámpa akkor megállok
 - ha zöld a lámpa akkor elindulok
 - ha fal van előttem akkor elfordulok
 - ha tudom, hogy nem megy akkor gyakorlom
 - ...
 - ha a bekért szám páros akkor kiíratom, hogy páros
   különben kiíratom, hogy páratlan
 - ha a dobókocka értéke 5 akkor előre lépek 5-öt

 Ismétlés - ciklus - (iteráció)
 - Addig menj, amíg a tábla van
 - Addig dobáld az aprót a gépbe, amíg el nem éred a megfelelő összeget
 - Üss bele 3 db tojást
 - Addig tegyél bele cukrot amíg elég édes nem lesz
 - Addig gyakorlok, amíg meg nem értem
 - Addig fog a tanár piszkálni, amíg nem látja, hogy értem
"""

db = 12
print("szám", db)
# a szám utolsó számjegye páros-e? 
utolso_szamjegy = db % 5
print("utolsó számjegy:", utolso_szamjegy)

if(utolso_szamjegy % 2 == 0):
    print("páros")
else:
    print("páratlan")


# db-nyi almát szeretnék látni
for kiskutya in range(0 ,db, 1):
  print("Alma", kiskutya+1)
  
szoveg = "Kalapács"
print(szoveg)

index = 0
for karakter in szoveg:
  print(karakter, index)
  index += 1