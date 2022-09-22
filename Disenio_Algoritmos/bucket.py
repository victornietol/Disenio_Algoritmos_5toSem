import math

def BucketSort(Lista):
    k = len(Lista)
    n = Lista[0]
    m = Lista[0]
    LO =[]

    for e in Lista:
        if(e < n):
            n = e
        if(e > m):
            m = e

    if(m-n > k*k):
        print("Mejor usa burbuja")
    elif(m-n > k*math.log(k)/math.log(2)):
        print("Mejor usa QuickSort")

    contenedores = []
    for i in range(m-n+1):
        contenedores.append(0)
    for e in Lista:
        contenedores[e-n]+=1

    indice = n
    for e in contenedores:
        for i in range(e):
            LO.append(indice)
        indice +=1
    return LO

lista = [5,4,5,0,0,0,8,12,0,12,7]
#lista = [13,22,14,21,17,15,18]
print(lista)
lista = BucketSort(lista)
print(lista)