import random

# Generáljon egy listába 13 db négyjegyű véletlen számokat, amik, 3, 5,7- re végződnek!
# Hány darab 3-ra, 5-re, és 7-re végződő szám van
"""
lista = []
listaszam = 0
while(listaszam < 13):
    listarand = random.randint(1000,9999)
    for index in range(0,listarand,4):
        if listarand[index] == 3:
            listaszam += 1
            lista.append(listarand)
        elif listarand[index] == 5:
            listaszam += 1
            lista.append(listarand)
        elif listarand[index] == 7:
            listaszam += 1
            lista.append(listarand)

    
print(lista)
"""
lista = []

for i in range(0,13,1):
    valtozo = random.randint(100,999)
    veletlen = random.randint(1,3)
    if(veletlen == 1):
        lista.append(valtozo*10+3)
    elif(veletlen == 2):
        lista.append(valtozo*10+5)
    else:
        lista.append(valtozo*10+7)
print(lista)

haromra = 0
otre = 0
hetre = 0
for i in range(0,len(lista),1):
    if(lista[i] % 10 == 3):
        haromra += 1
    elif(lista[i] % 10 == 5):
        otre += 1
    else:
        hetre += 1
print("Háromra végződik",haromra)
print("Ötre végződik",otre)
print("Hétre végződik",hetre)

# számtani átlag
# hány darab szám van átlag alatt 
# mértani átlag
# a mértani átlag alatti számok összege
# 30db 13, 17 re végződő számokkal, hány osztható 13-mal és 17-tel
# bekérsz egy hosszann szöveget, hány darab felhasználó által megadott betű van benne 
# bekérsz két szót, mond meg adott indexen hány darab betű eltérés van(pl. alma, alkat -> 2 darab különbség)
# 