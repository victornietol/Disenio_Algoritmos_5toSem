import random 

def BB(Lista, dato):
    n = len(Lista)
    if(n>1):
        k = int(len(Lista) / 2)
        m = Lista[k]
        if(m == dato):
            print('Se encontró el dato', m)
            return True
        elif(m < dato):
            ListaM = Lista[k:]
            BB(ListaM, dato)
        elif(m > dato):
            ListaM = Lista[:k]
            BB(ListaM, dato)
    elif(n == 1):
        if(Lista[0] == dato):
            print('Se encontró el dato', Lista[0])
            return True
        else:
            print('No se encontró el dato')
            return False
    else:
        print('No se encontró el dato')
        return False

a = 50
b = 500
i = 2
Lista = list(range(a,b,i))
n = random.randint(a,b)
print(n)
BB(Lista,n)