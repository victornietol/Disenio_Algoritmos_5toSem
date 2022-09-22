def peorOrd(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if(lista[j+1] > lista[j]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
            lista_rev = list(reversed(lista))
    return lista_rev



def peorOrd2(lista):
    lista_rev = []
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if(lista[j+1] > lista[j]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
        lista_rev.insert(0,lista[i])
    return lista_rev

lista = [11,1,4,2,10,3,6,9,5,7,12,8]
res = peorOrd(lista)
print(res)