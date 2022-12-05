"""
El problema se planteó de la siguiente forma: Cada individuo tiene 4 dígitos (12 bits), por lo tanto, cada dígito se 
representa con 3 bits porque el dígito puede ir de 1 a 8 y con esto nos quedan en total 12 bits. Por otro lado, la 
posición de cada dígito se asigna con los valores de una lista donde cada vez que se ocupa una posición se elimina 
dicha posición de la lista con el objetivo de evitar las repeticiones en cuanto a la posición. Por lo tanto, la
correspondencia es la siguiente: 000 -> 1, 001 -> 2, 010 -> 3, 011 -> 4, 100 -> 5, 101 -> 6, 110 -> 7, 111 -> 8
"""

import numpy as np
import random

class AlgoritmoGenetico:
    def __init__(self,codigo):
        self.codigo = codigo
        self.digitoEncontrado = []
    
    # Generado de forma binaria la población que se utiliza en el algoritmo genético        

    def generaPoblacion(self,nInd,tam):
        return np.random.randint(0,2,(nInd,tam))
    
    # Pasando de binario a decimal cada individuo, sin que sea su representación final aún

    def binarioADecimal(self,binario):
        exp=len(binario)-1
        decimal = 0
        for bit in binario:
            decimal+=bit*(np.power(2,exp))
            exp-=1
        return decimal
    
    # Pasando cada individuo de su forma decimal a su representación en dígito final planteada para este problema

    def bitsADigito(self,d):  
        n = self.binarioADecimal(d) 
        digito = n+1
        return digito
    
    # Pasando de genotipo a fenotipo, donde cada individuo (código) se guarda en una lista que contiene otras 4 listas, 
    # cada una con un dígito y su posición, por lo tanto, se guardan así [ [dígito,posición], [d,p], [d,p], [d,p] ]
    
    def genotipoAFenotipo(self,individuo):  
        numerosEnBits = []
        C = []
        posiciones = [0,1,2,3]
        for i in range(4):
            numerosEnBits.append(individuo[i*3:(i+1)*3])
        for d in numerosEnBits:
            posicion = random.choice(posiciones) # Asignando una posición al azar
            posiciones.remove(posicion)
            C.append([self.bitsADigito(d),posicion])
        return C
    
    # Realizado la cruza para el proceso evolutivo del algoritmo genético con un punto de cruza generado al azar

    def cruza(self,indA,indB):
        puntoCruza = np.random.randint(len(indA))
        desc1 = list(indA[0:puntoCruza])+list(indB[puntoCruza:])
        desc2 = list(indB[0:puntoCruza])+list(indA[puntoCruza:])
        return desc1, desc2
    
    # Proceso de mutación de un individuo seleccionado al azar para el proceso evolutivo del algoritmo genético

    def muta(self,ind):
        puntoMutacion = np.random.randint(len(ind))
        ind[puntoMutacion] = 1-ind[puntoMutacion]  # Si el bit del individuo es 0 cambia a 1 y viceversa
        return ind
    
    # Revisa las posiciones de cada dígito de un código para poder rankear a cada individuo en la evaluación de cada código
    
    def valorarAB(self,numero):
        a = 0   # a) Dígitos en posición correcta
        b = 0   # b) Dígitos en posición incorrecta
        for i,d in zip(numero,self.codigo):
            if(i==d):
                a+=1
            else:
                if(i in self.codigo):
                    b+=1
        return a, b
    
    # Asigna el dígito a otra variable para poder valorar el individuo según la posición de sus dígitos y regresa
    # el número de dígitos en posició correcta (a) y el número de dígitos en posición incorrecta (b)
    
    def verificarDigitos(self,C):
        numero = [0,0,0,0]
        for i in C:
            numero[i[1]] = i[0]  # Acomodando dígitos en posición
        a,b = self.valorarAB(numero)
        return a, b
    
    # Calificando al individuo dependiendo de la posición de sus dígitos

    def evaluaNumero(self,C):  
        a,b = self.verificarDigitos(C)
        
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
            self.digitoEncontrado = C
            return 14
        
    # Pasa al individuo de su forma en bits a dígitos y después lo evalua

    def evaluarInd(self,ind):
        C = self.genotipoAFenotipo(ind)
        evaluacion = self.evaluaNumero(C)
        return evaluacion
    
    # Valora la población y guarda la evaluación de cada individuo en una lista

    def evaluaPoblacion(self,poblacion):
        evaluacion = []
        for ind in poblacion:
            evaluacion.append(self.evaluarInd(ind))
        return evaluacion
    
    # Genera los índices para la cruza y con ello generar los dos descendientes

    def buscaIndices(self,prob):
        a = 0
        n = np.random.random()
        while(n>prob[a]):
            a+=1
        b = 0
        n = np.random.random()
        while(n>prob[b]):
            b+=1
        return a, b
    
    # Recorre todas las evaluaciones y busca la correspondiente al mejor individuo y al peor individuo (evaluación más alta y más baja)

    def buscaMejorPeor(self,evaluacion):
        mejor = 0
        peor = 0
        for i in range(len(evaluacion)):
            if(evaluacion[i]>evaluacion[mejor]):
                mejor = i
            if(evaluacion[i]<evaluacion[peor]):
                peor = i
        return mejor, peor
    
    # Realiza el proceso evolutivo del algoritmo genético generando una nueva población como resultado de la cruza 
    # y en ciertas ocasiones también se realiza mutación dependiendo de un valor al azar
    
    def procesoEvolutivo(self,poblacion,evaluacion,tam):
        nuevaPoblacion = []
        evaluacion = list(np.array(evaluacion)/sum(evaluacion))
        prob = [evaluacion[0]]
        for i in range(len(evaluacion)-1):
            prob.append(prob[-1]+evaluacion[i+1])
        while(len(nuevaPoblacion)<(tam-2)):
            a,b = self.buscaIndices(prob)
            desc1,desc2 = self.cruza(poblacion[a],poblacion[b])
            if(np.random.random()<0.07):
                if(np.random.random()<0.5):
                    desc1 = self.muta(desc1)
                else:
                    desc2 = self.muta(desc2)
            nuevaPoblacion.append(desc1)
            nuevaPoblacion.append(desc2)
        mejor,peor = self.buscaMejorPeor(evaluacion)
        nuevaPoblacion.append(poblacion[mejor])
        nuevaPoblacion.append(poblacion[peor])
        return nuevaPoblacion
    
    # Inicio del algoritmo genético dependiendo del número de individuos, el tamaño de cada individuo y el número de generaciones

    def algoritmoGen(self,nInd,tam,nMaxGen):
        poblacion = self.generaPoblacion(nInd,tam)
        Gen = 0
        while(Gen<nMaxGen):
            evaluacion = self.evaluaPoblacion(poblacion)
            nuevaPoblacion = self.procesoEvolutivo(poblacion,evaluacion,tam)
            poblacion = nuevaPoblacion
            Gen+=1
        return self.digitoEncontrado
    
    
class Juego:
    def __init__(self):
        self.encontrado = False
        self.codigo = self.generarCodigo()
        print("Código original: ",self.codigo,end="\n\n")
        
    # Generando de forma aleatoria el código de 4 dígitos, donde cada dígito puede ir desde 1 a 8

    def generarCodigo(self):
        codigo = []
        for i in range(4):
            codigo.append(np.random.randint(1,9))    
        return codigo
    
    # Acomodando el dígito según su posición 
    
    def acomodarDigito(self,digitos):
        numero = [0,0,0,0]
        try:    
            for i in digitos:
                numero[i[1]] = i[0]  # Acomodando digitos en posición
            return numero
        except NameError:
            pass
    
    # Inicio del juego, en cada intento buscará encontrar el código con el algoritmo genético
    
    def jugar(self):
        aux = 1
        resultado = []
        while(not self.encontrado):
            print("Intento ",aux)
            aux+=1
            AG = AlgoritmoGenetico(self.codigo)
            digitos = AG.algoritmoGen(1000,12,1000)
            resultado = self.acomodarDigito(digitos)
            if(resultado==self.codigo):
                self.encontrado = True
                print("Código ENCONTRADO: ",resultado)
            else:
                print("Código no encontrado",end="\n\n")

            
# Ejecutando el juego         
            
juego = Juego()
juego.jugar()