import random
inputszam = ""
szam = random.randint(10,99)
probalkozasok = 0
print("Gondoltam egy kétjegyű számra, találd ki!")
while(inputszam != szam):
    probalkozasok += 1
    inputszam = int(input("Szám: "))
    if(inputszam > 9 and inputszam < 100): 
        if inputszam == szam:
            print("Eltaláltad!")
        elif inputszam < szam:
            print("A gondolt szám nagyobb!")
        elif inputszam > szam:
            print("A gondolt szám kisebb!")
    else:
        print("Nem kétjegyű számot adott meg!")
        szam = int(input("Próbálkozzon mégegyszer: "))   
print()
print("Próbálkozások száma: ",probalkozasok)



