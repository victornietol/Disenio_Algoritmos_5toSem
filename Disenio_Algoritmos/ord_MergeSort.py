def MergeSort(lista):
    if (len(lista) > 1):
        lista1, lista2 = dividirMitad(lista)
        lista1, lista2 = MergeSort(lista1), MergeSort(lista2)
        lista = Merge(lista1, lista2)
    return lista

def dividirMitad(lista):
    n = len(lista)
    m = n//2
    return lista[:m] , lista[m:]

def Merge(lista1, lista2):
    resultado = []
    while (len(lista1)>0 and len(lista2)>0):
        if (lista1[0] < lista2[0]):
            resultado.append(lista1[0])
            lista1.remove(lista1[0])
        else:
            resultado.append(lista2[0])
            lista2.remove(lista2[0])
    return resultado + lista1 + lista2

# Probando código

lista = [6,8,4,3,5,1,2,9,7]
print(lista)

print(MergeSort(lista))