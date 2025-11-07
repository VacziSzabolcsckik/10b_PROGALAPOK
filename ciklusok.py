import random as r
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
print()

szoveg[0]
szoveg[1]
szoveg[2]
for  index in range (0, len(szoveg)-1, 1):
    print(szoveg[index]+",",end=" ")
#print(szoveg[len(szoveg)-1])
print(szoveg[-1])

# 30-50-ig 4-gyel osztható számok

for elem in range(32, 50, 4):
    print(elem, end=" ")
print()

# 10-től 1-ig

for szam in range(10, 0, -1):
    print(szam, end=" ")
print() 

# scápalak

for index in range(len(szoveg)-1, -1, -1):
    print(szoveg[index], end=" ")
print()

n = len(szoveg)
for index in range(-1, -n-1, -1):
    print(szoveg[index],end=" ")
print()

# írassa ki a szöveget az indexével társítva! (1k 2a 3l 4a 5p 6á 7c 8s)


for index in range (0, n, 1):
    print(str(index+1)+szoveg[index], end=" ")
    print()

# írasson ki 5db véletlen karaktert a szövegből!
for db in range(0,5,1):
    szam = r.randint(0,n-1)
    print(szoveg[szam], end=" ")
print()


ujszoveg = ""
for index in range(-1, -n-1, -1):
    ujszoveg += szoveg[index]
    #print(szoveg[index],end=" ")
print(ujszoveg)