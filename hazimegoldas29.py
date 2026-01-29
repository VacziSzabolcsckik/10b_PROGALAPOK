import random
import math

def listafeltolt(n):
    lista = []
    for i in range(0,n,1):
        #lista.append(random.randint(200,900)/100)
        lista.append(round(random.random()*7+2, 2)) # [0,1]*(9-2)+2
    return lista

def vaneszamnalnagyobb(szam, lista):
    index = 0
    while(index < len(lista) and lista[index] <= szam):
        index += 1
    vane = index < len(lista)
    return vane

def vaneketszamkozott(a, b, lista):
    index = 0
    while(index < len(lista) and not (lista[index] >= a and lista[index] <= b)):
    #while(index < len(lista) and not (lista[index] >= a and lista[index]>=b)):
    #Ttul: lista[index] > szam NEM Ttul: lista[index] > szam
        index += 1
    vane = index < len(lista)
    return vane


def main():
    jancsi = []
    juliska = []
    # db = int(input())
    # db = random.randint(12,96)
    # print(listafeltolt(14))
    jancsi = listafeltolt(14)
    juliska = listafeltolt(14)
    print("Juliska: ", juliska)
    print("Jancsi: ", jancsi)
    vanejuliska = vaneszamnalnagyobb(8.5, juliska)
    if(vanejuliska):
        print("Van Juliskánál 8.5-nél nagyobb")
    else:
        print("Nincs Juliskánál 8.5-nél nagyobb")

    vanejancsi = vaneszamnalnagyobb(8.5, jancsi)
    if(vanejancsi):
        print("Van Jancsinál 8.5-nél nagyobb")
    else:
        print("Nincs Jancsinál 8.5-nél nagyobb")
    
    juliskaosszeg = 0

    for i in range(0,len(juliska),1):
        juliskaosszeg += juliska[i]
    
    juliskaatlag = juliskaosszeg / 14
    print("Juliska átlaga",round(juliskaatlag,2))

    jancsiosszeg = 0

    for i in range(0,len(jancsi),1):
        jancsiosszeg += jancsi[i]
    
    jancsiatlag = jancsiosszeg / 14
    print("Jancsi átlaga",round(jancsiatlag,2))

    vanejuliskakozott = vaneketszamkozott(4.9, 5.1, juliska)
    if(vanejuliskakozott):
        print("Juliskának van 4.9 és 5.1 közötti értéke")
    else:
        print("Juliskának nincs 4.9 és 5.1 közötti értéke")

    vanejancsikozott = vaneketszamkozott(4.9, 5.1, jancsi)
    if(vanejancsikozott):
        print("Jancsinak van 4.9 és 5.1 közötti értéke")
    else:
        print("Jancsinak nincs 4.9 és 5.1 közötti értéke")


main()