# 1. Írjon egy függvényt ami bekér a felhasználótól egy számot, 10 és 20 között úgy, hogyha rossz értéket adorr meg ismételje meg a bekérést! Adja vissza a bekért helyes értéket!
# 2. Írjon egy fv-t ami visszaad egy listát. A korábban bekért szám legyen a darabszám. A számok pedig 2 jegyű de 4-gyel nem osztható számok!
#3. Írjon egy fv-t ami visszaadja a lsitából az első 7-re végződő számot, ha van ilyen

import random

def szambekeres():
    szam=int(input("Adjon meg egy számot  10 és 20 között: "))
    while szam < 10 or szam > 20:
        szam = int(input("Hiba! Adjon meg újra egy számot ami 10 és 20 között van: "))
    return szam 

def listavisszaadasa(szam):
    lista = []
    while szam > len(lista):
        listadas = random.randint(10,99)
        if listadas % 4 != 0:
            lista.append(listadas)
    return lista

def hetrevegzodo(lista):
    bekertszam = szambekeres()
    i = 0
    while(i < len(lista) and  lista[i] % 10 != 7):
        i+=1
    
    hetre = i < len(lista)
    if hetre:
        return i
    else:
        return -1

def main():
    bekertszam = szambekeres()
    print(bekertszam)  
    lista = listavisszaadasa(bekertszam)
    print(lista)
    index = hetrevegzodo(lista)
    if(index == -1):
        print("Nincs a listában 7-tel osztható elem")
    else:
        print("Van a listában 7-tel osztható elem, az", index+1, "helyen")
main()

