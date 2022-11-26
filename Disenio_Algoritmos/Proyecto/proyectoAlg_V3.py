import numpy as np
import random

def generarCodigo():
    global codigo
    codigo=[]
    for i in range(4):
        codigo.append(np.random.randint(1,9))


def generaPoblacion(nInd,tam):
    return np.random.randint(0,2,(nInd,tam))

def binarioADecimal(binario):
    exp=len(binario)-1
    decimal = 0
    for bit in binario:
        decimal+=bit*(np.power(2,exp))
        exp-=1
    return decimal

def bitsACarta(c):  #bitsADigito
    n=binarioADecimal(c) 
    digito=n+1
    return digito
    
def genotipoAFenotipo(individuo):  #
    cartasEnBits=[]
    posiciones=[0,1,2,3]
    for i in range(4):
        cartasEnBits.append(individuo[i*3:(i+1)*3])
    C=[]
    for c in cartasEnBits:
        posicion=random.choice(posiciones) #generando posiciones
        posiciones.remove(posicion)
        C.append([bitsACarta(c),posicion])
    return C

def cruza(indA,indB):
    puntoCruza=np.random.randint(len(indA))
    desc1=list(indA[0:puntoCruza])+list(indB[puntoCruza:])
    desc2=list(indB[0:puntoCruza])+list(indA[puntoCruza:])
    return desc1,desc2

def muta(ind):
    puntoMutacion=np.random.randint(len(ind))
    ind[puntoMutacion]=1-ind[puntoMutacion]
    return ind

    
def intento(numero):
    a=0   # a) Dígitos en posición correcta
    b=0   # b) Dígitos en posición incorrecta
    for i,c in zip(numero,codigo):
        if(i==c):
            a+=1
        else:
            if(i in codigo):
                b+=1
    return a,b
    
def verificarDigitos(C):
    numero=[0,0,0,0]
    for i in C:
        numero[i[1]]=i[0]  # Acomodando digitos en posición
    a,b=intento(numero)
    return a,b
    

def evaluaMano(C):  ## evaluarNumero
    #valor=0 
    global digitoEncontrado
    a,b=verificarDigitos(C)
    
    if(a==0 and b==0):
        return 0
    elif(a==0 and b==1):
        return 1
    elif(a==0 and b==2):
        return 2
    elif(a==0 and b==3):
        return 3
    elif(a==0 and b==4):
        return 4
    elif(a==1 and b==0):
        return 5
    elif(a==1 and b==1):
        return 6
    elif(a==1 and b==2):
        return 7
    elif(a==1 and b==3):
        return 8
    elif(a==2 and b==0):
        return 9
    elif(a==2 and b==1):
        return 10
    elif(a==2 and b==2):
        return 11
    elif(a==3 and b==0):
        return 12
    elif(a==3 and b==1):
        return 13
    elif(a==4 and b==0):
        digitoEncontrado = C
        return 14
      

def evaluarInd(ind):
    C=genotipoAFenotipo(ind)
    evaluacion = evaluaMano(C)
    return evaluacion

def evaluaPoblacion(poblacion):
    evaluacion=[]
    for ind in poblacion:
        evaluacion.append(evaluarInd(ind))
    return evaluacion

def buscaIndices(prob):
    a=0
    n=np.random.random()
    while(n>prob[a]):
        a+=1
    b=0
    n=np.random.random()
    while(n>prob[b]):
        b+=1
    return a,b

def buscaMejorPeor(evaluacion):
    mejor=0
    peor=0
    for i in range(len(evaluacion)):
        if(evaluacion[i]>evaluacion[mejor]):
            mejor=i
        if(evaluacion[i]<evaluacion[peor]):
            peor=i
    return mejor,peor

def procesoEvolutivo(poblacion,evaluacion,tam):
    evaluacion = list(np.array(evaluacion)/sum(evaluacion))
    prob=[evaluacion[0]]
    for i in range(len(evaluacion)-1):
        prob.append(prob[-1]+evaluacion[i+1])
    nuevaPoblacion=[]
    while(len(nuevaPoblacion)<(tam-2)):
        a,b=buscaIndices(prob)
        desc1,desc2=cruza(poblacion[a],poblacion[b])
        if(np.random.random()<0.07):
            if(np.random.random()<0.5):
                desc1=muta(desc1)
            else:
                desc2=muta(desc2)
        nuevaPoblacion.append(desc1)
        nuevaPoblacion.append(desc2)
    mejor,peor=buscaMejorPeor(evaluacion)
    nuevaPoblacion.append(poblacion[mejor])
    nuevaPoblacion.append(poblacion[peor])
    return nuevaPoblacion
    

def AG(nInd,tam,nMaxGen):
    poblacion=generaPoblacion(nInd, tam)
    Gen=0
    while(Gen<nMaxGen):
        evaluacion=evaluaPoblacion(poblacion)
        nuevaPoblacion=procesoEvolutivo(poblacion,evaluacion,tam)
        poblacion=nuevaPoblacion
        Gen+=1
    mejor,peor=buscaMejorPeor(evaluacion)
    C=genotipoAFenotipo(poblacion[mejor])
    return C
    

# Inicio del juego

encontrado = False
aux = 1
generarCodigo()
print("Código original: ",codigo,end="\n\n")

while(not encontrado):
    print("Intento ",aux)
    aux+=1
    C=AG(1000,12,1000)
    try:
        numero=[0,0,0,0]
        for i in digitoEncontrado:
            numero[i[1]]=i[0]  # Acomodando digitos en posición
        encontrado = True
        print("Código ENCONTRADO: ",numero)
    except NameError:
        print("Código no encontrado",end="\n\n")