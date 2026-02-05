# HF 
# Szimuláljon egy matematika versenyt és az eredményeire készített statisztikát! Mind a 17 diák nagyon ügyes, így kevés rossz verseny dolgozat született. A döntőbe jutásésrt 70%-ot el kell érni.
# 1. Készítsen egy függvényt, amit feltölt egy listát úgy, hogy 50%-os eseéllyel szülessenek 120-200 közötti pontok, a maradék pedig 50-120 közötti pont legyen!
# 2. Írjon függvényt, ami visszaadja a versenydolgozatok átlagát!
# 3. Írjon függvényt, ami visszaadja a versenydolgozatok terjedelmét!
# 4. Írjon függvényt, ami visszaadja lett-e maximum pontos?
# 5. Írjon függvényt, ami visszaadja hány versenyző jutott a döntőbe?
# 6. Írjon függvényt, ami visszaadja, hogy volt-e 50 pontos, ha volt hányadik tanuló?
import random


def listafeltoltes():
    lista = []
    for i in  range(0,17,1):
        valsz = random.randint(0,100)
        if(valsz >= 50):
            lista.append(random.randint(120,200))
        else:
            lista.append(random.randint(50,120))
    return lista

def listaatlag(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i]
    atlag = osszeg/len(lista)
    return atlag

def listamaximuma(lista):
    maxe = lista[0]
    for i in range(1,len(lista),1):
        if(lista[i]>maxe):
            maxe = lista[i]
    return maxe

def listaminimuma(lista):
    mine = lista[0]
    for i in range(1,len(lista),1):
        if(lista[i]<mine):
            mine = lista[i]
    return mine

def listaterjedelme(lista):
    maximum = listamaximuma(lista)
    minimum = listaminimuma(lista)
    return maximum - minimum

def listamaxpontos(lista):
    n = 200
    index = 0
    while(index<len(lista) and not n == lista[index]):
        index += 1
    vane = index < len(lista)
    return vane

def listatovabbjut(lista):
    index = 140
    jute = 0
    for i in range(0,len(lista),1):
        if lista[i] >= index:
            jute += 1
    return jute

def listaotvenpont(lista):
    index = 0
    while(index < len(lista) and not lista[index] == 50):
        index += 1
    vane = index < len(lista)
    if vane:
        return index+1
    else:
        return -1


def main():
    # 1. feladat
    pontok = listafeltoltes()
    print(pontok)

    # 2. feladat
    atlag = listaatlag(pontok)
    print("Átlag: ", round(atlag,2))

    # 3. feladat
    terjedelem = listaterjedelme(pontok)
    print("Terjedelem: ",terjedelem)

    # 4. feladat
    maxpont = listamaxpontos(pontok)
    if(maxpont):
        print("Van max pontos")
    else:
        print("Nincs max pontos")

    # 5. feladat
    tovabbjut = listatovabbjut(pontok)
    print("Döntőbe továbbjutók száma: ",tovabbjut)

    # 6. feladat
    otvenpont = listaotvenpont(pontok)
    if otvenpont != -1 :
        print("Ezen a helyen van benne ötven pontos: ", otvenpont)
    else:
        print("Nincs ötven pontos")
main()