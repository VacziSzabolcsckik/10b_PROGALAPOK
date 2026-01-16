import random

"""
Függvények
Scrath blokkok

Előre definiált folyamatok, amit külső értéktől függően, végrehajtják a belső utasításokat

def fuggvenyNev():
    Függvény tartalma

fuggvenyNev() fuggveny meghivasa
"""

#Általában kiíratás soran hasznaljuk
# osszeadas fuggveny definiálása
def osszeadas():
    a = 12
    b = 17
    print(a+b)

# osszeadas kulso ertektol fuggoen PARAMETEREN keresztul
def osszeadasParam(a,b):
    c = a+b
    print(c)

# osszeadas fuggveny meghivasa
osszeadas()
osszeadasParam(15,17)



#visszateressel rendelkezo fuggvenyek
def kettoatizediken():
    # a = math.pow(2, 10)
    a = 2 ** 10
    return a

valtozo = kettoatizediken()
print(valtozo)

def osszeadasvisszaterese(a,b):
    c=a+b
    return c

print(osszeadasvisszaterese(13,17))
 

def veletlenszamkiiratas(db):
    for i in range(0,db,1):
        print(random.randint(100,999), end=" ")

veletlenszamkiiratas(10)

# ˇ> [ÄŁäĐä]
print()


def szovegvisszafele(szo):
    for i in range(len(szo)-1,-1,-1):
        print(szo[i], end="")

szovegvisszafele("gorog")
print()

# ^> [ÄŁäĐä] ł$đ<đÄ} Ä]> [¨]]@$}>; ä<Í [¨]] Ä]> đ˝@Ä]÷Ł; $đ @ÍđđääĐíä ä đ¸@Íđđä[ÄŁÄ] 

def szovegVisszafelefv(szoveg):
    visszaszoveg = ""
    for index in range(len(szoveg)-1,-1,-1):
        visszaszoveg += szoveg[index]
    return visszaszoveg

print(szovegVisszafelefv("kipkiop"))
print()

# írjon egy függvényt ami egy szorol eldonti hogy palindrom e és vissza adja válaszul?

def palindrom(szo):
    if(szo == szovegVisszafelefv(szo)):
        return("palindrom")
    else:
        return("nem palindrom")

print(palindrom("aba"))

"""
palindrom("gorog")
    if vissza == szo:
        print("A szó palindrom")
    else:
        print("A szó nem palindrom")
"""    """
    i=0
    while(i<=len(szo)//2 and szo[i] == szo[len(szo)-1-i]):
        i+=1
    if(i>len(szo)//2):
        return "palindrom"
    else:
        return "nem palindrom"
"""