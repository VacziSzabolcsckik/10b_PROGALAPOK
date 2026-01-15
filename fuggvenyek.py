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