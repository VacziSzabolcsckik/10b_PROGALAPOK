"""
Ciklusok - Ismétlés - Loop

Számlálás - For ciklus
Végig megy a megadott elemeken vagy intervallumon!
for elem in range(mettol, meddig, hányasával):
    Ismétlendő folyamat

for karakter in szoveg:
    Ismétlendő folyamat


Tesztelős - While

"""

# [1,10[ ig a számok
for elem in range(1, 11, 1):
    print(elem,end=" ")

# első 10 db páros szám
for elem in range(0, 19, 2):
    print(elem,end=" ")

# szöveg betűi közé vesszőt
szoveg = "kalapács"
print(szoveg)
for karakter in szoveg:
    print(karakter, end=",")
