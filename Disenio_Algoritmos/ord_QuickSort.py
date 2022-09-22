def QuickSort(L):
    if (len(L) > 1 and verificarIguales(L)):
        piv = selPiv(L)
        menoresL, mayoresL = divL(L, piv)
        menoresL, mayoresL = QuickSort(menoresL), QuickSort(mayoresL)
        return menoresL + mayoresL
    else:
        return L

def selPiv(L):
    suma = 0
    for e in L:
        suma+= e
    return suma / len(L)

def divL(L, piv):
    menoresL = []
    mayoresL = []
    for e in L:
        if (e < piv):
            menoresL.append(e)
        else:
            mayoresL.append(e)
    return menoresL, mayoresL

def verificarIguales(L):
    if (len(L) >= 1):
        anterior = L[0]
        for e in L:
            if (not e == anterior):
                return True
        return False
    else:
        return False

# Probando código

L = [4,8,5,7,1,2,9,3,6]
print(L)

print(QuickSort(L))