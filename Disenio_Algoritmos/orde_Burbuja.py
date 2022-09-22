def burbuja(lista):
    for i in range(1,len(lista)):
        for j in range(0,(len(lista)-i)):
            if lista[j+1] < lista[j]:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux
    print(lista)

# Probando código

lista = [6,5,3,1,8,7,2,4,9]
print(lista)
burbuja(lista)