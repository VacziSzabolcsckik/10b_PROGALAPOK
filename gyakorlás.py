# 0.kérjen be egy szöveget és egy betűt!
# 0.5 Nézze meg van-e a szövegben az adott betű, ha van 
# 1. adja meg hány darab betű van a szövegben!

szoveg = input("Adjon meg egy szöveget: ")
betu = input("Adjon meg egy betűt: ")
"""
indexu = ""
for index in range(0, len(szoveg), 1):
    index += len(szoveg)+1
    indeksz = index-len(szoveg)
    indexu += indeksz[-1]
    print(indexu, end=" ")
"""
index = 0
while(index < len(szoveg) and szoveg[index] != betu):
    index += 1
print(index)

if(index < len(szoveg)):
  
db = 0
for karakter in szoveg:
    if(karakter == betu):
        db+=1
print(db)