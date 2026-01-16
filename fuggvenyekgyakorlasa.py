import random

# Készítsen egy függvényt amely egy darab számtól függ és visszaad egy feltöltött listát [-10,50] közötti számokkal
#készítsen egy fuggvenyt ami barmilyen lista elemeit megvizsgalva visszaadja hogy hany darab pozitiv szam van
def szlista(db):
    lista = []
    for i in range(0,db,1):
        lista.append(random.randint(-10, 50))
    return lista

def main():
    lista = szlista(13)
    print(lista)

    pozitiv = 0
    for i in range(0,len(lista),1):
        if lista[i] >= 0:
            pozitiv += 1
    return pozitiv            
main()

print(main())