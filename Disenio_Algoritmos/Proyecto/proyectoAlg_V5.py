"""
El problema se planteó de la siguiente forma: Cada individuo tiene 4 dígitos (12 bits), por lo tanto, cada dígito se 
representa con 3 bits porque el dígito puede ir de 1 a 8 y con esto nos quedan en total 12 bits. Por otro lado, la 
posición de cada dígito se asigna con los valores de una lista donde cada vez que se ocupa una posición se elimina 
dicha posición de la lista con el objetivo de evitar las repeticiones en cuanto a la posición. Por lo tanto, la
correspondencia es la siguiente: 000 -> 1, 001 -> 2, 010 -> 3, 011 -> 4, 100 -> 5, 101 -> 6, 110 -> 7, 111 -> 8
"""

import numpy as np
import random

# Generando de forma aleatoria el código de 4 dígitos, donde cada dígito puede ir desde 1 a 8

def generarCodigo():
    global codigo
    codigo=[]
    for i in range(4):
        codigo.append(np.random.randint(1,9))

# Generado de forma binaria la población que se utiliza en el algoritmo genético        

def generaPoblacion(nInd,tam):
    return np.random.randint(0,2,(nInd,tam))

# Pasando de binario a decimal cada individuo, sin que sea su representación final aún

def binarioADecimal(binario):
    exp=len(binario)-1
    decimal = 0
    for bit in binario:
        decimal+=bit*(np.power(2,exp))
        exp-=1
    return decimal

# Pasando cada individuo de su forma decimal a su representación en dígito final planteada para este problema

def bitsADigito(d):  
    n=binarioADecimal(d) 
    digito=n+1
    return digito

# Pasando de genotipo a fenotipo, donde cada individuo (código) se guarda en una lista que contiene otras 4 listas, 
# cada una con un dígito y su posición, por lo tanto, se guardan así [ [dígito,posición], [d,p], [d,p], [d,p] ]

def genotipoAFenotipo(individuo):  
    numerosEnBits=[]
    posiciones=[0,1,2,3]
    for i in range(4):
        numerosEnBits.append(individuo[i*3:(i+1)*3])
    C=[]
    for d in numerosEnBits:
        posicion=random.choice(posiciones) # Asignando una posición al azar
        posiciones.remove(posicion)
        C.append([bitsADigito(d),posicion])
    return C

# Realizado la cruza para el proceso evolutivo del algoritmo genético con un punto de cruza generado al azar

def cruza(indA,indB):
    puntoCruza=np.random.randint(len(indA))
    desc1=list(indA[0:puntoCruza])+list(indB[puntoCruza:])
    desc2=list(indB[0:puntoCruza])+list(indA[puntoCruza:])
    return desc1,desc2

# Proceso de mutación de un individuo seleccionado al azar para el proceso evolutivo del algoritmo genético

def muta(ind):
    puntoMutacion=np.random.randint(len(ind))
    ind[puntoMutacion]=1-ind[puntoMutacion]  # Si el bit del individuo es 0 cambia a 1 y viceversa
    return ind

# Revisa las posiciones de cada dígito de un código para poder rankear a cada individuo en la evaluación de cada código
    
def valorarAB(numero):
    a=0   # a) Dígitos en posición correcta
    b=0   # b) Dígitos en posición incorrecta
    for i,d in zip(numero,codigo):
        if(i==d):
            a+=1
        else:
            if(i in codigo):
                b+=1
    return a,b

# Asigna el dígito a otra variable para poder valorar el individuo según la posición de sus dígitos y regresa
# el número de dígitos en posició correcta (a) y el número de dígitos en posición incorrecta (b)

def verificarDigitos(C):
    numero=[0,0,0,0]
    for i in C:
        numero[i[1]]=i[0]  # Acomodando dígitos en posición
    a,b=valorarAB(numero)
    return a,b
    
# Calificando al individuo dependiendo de la posición de sus dígitos

def evaluaNumero(C):  
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

# Pasa al individuo de su forma en bits a dígitos y después lo evalua

def evaluarInd(ind):
    C=genotipoAFenotipo(ind)
    evaluacion = evaluaNumero(C)
    return evaluacion

# Valora la población y guarda la evaluación de cada individuo en una lista

def evaluaPoblacion(poblacion):
    evaluacion=[]
    for ind in poblacion:
        evaluacion.append(evaluarInd(ind))
    return evaluacion

# Genera los índices para la cruza y con ello generar los dos descendientes

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

# Recorre todas las evaluaciones y busca la correspondiente al mejor individuo y al peor individuo (evaluación más alta y más baja)

def buscaMejorPeor(evaluacion):
    mejor=0
    peor=0
    for i in range(len(evaluacion)):
        if(evaluacion[i]>evaluacion[mejor]):
            mejor=i
        if(evaluacion[i]<evaluacion[peor]):
            peor=i
    return mejor,peor

# Realiza el proceso evolutivo del algoritmo genético generando una nueva población como resultado de la cruza 
# y en ciertas ocasiones también se realiza mutación dependiendo de un valor al azar

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
    
# Inicio del algoritmo genético dependiendo del número de individuos, el tamaño de cada individuo y el número de generaciones

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
generarCodigo() # Genera el código a encontrar
print("Código original: ",codigo,end="\n\n")

# El algoritmo genético se ejecutará mientras no se encuentre el código, una vez que se encuentre se mostrará

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