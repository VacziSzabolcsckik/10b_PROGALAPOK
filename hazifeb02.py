import random

def kartyageneralas():
    lista = []
    for i in range(1, 14, 1):
        lista.append("T"+str(i))
        lista.append("P"+str(i))
        lista.append("K"+str(i))
        lista.append("S"+str(i))
    return lista

def keveres(pakli):
    for i in range(10):
        a = random.randint(0,len(pakli)-1)
        b = random.randint(0,51)
        sv = pakli[a]
        pakli[a] = pakli[b]
        pakli[b] = sv

def lapindexe(lap, pakli):
    index = 0
    while pakli[index] != lap:
        index+=1
    #c.v.
    #vissza: index
    return index

def main():
    pakli = kartyageneralas()
    #print(pakli)
    keveres(pakli)
    print(pakli)
    lap = input("Adjon meg egy lapot - T,P,S,K + [1,13] (pl P1): ")
    index = lapindexe(lap, pakli)
    print(index+1)
main()