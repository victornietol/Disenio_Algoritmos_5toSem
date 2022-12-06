"""
El problema se planteó de la siguiente manera: Cada individuo tiene 4 dígitos (20 bits en total). En consecuencia cada
dígito consta de 5 bits donde los primeros 2 bits corresponden a la posición y los 3 siguientes al valor del dígito. 
Por lo tanto, cada dígito se representa con 3 bits porque el dígito puede ir de 1 a 8. Mientras que la posición de cada 
dígito se asigna con los elementos de una lista con valores en decimal donde cada vez que se ocupa una posición se elimina 
dicha posición de la lista con el objetivo de evitar las repeticiones en cuanto a la posición y posteriormente se convierte 
a binario. Por lo tanto, la correspondencia en cuanto a el valor de los dígitos y la posición es la siguiente: 
    Dígitos: 000 -> 1, 001 -> 2, 010 -> 3, 011 -> 4, 100 -> 5, 101 -> 6, 110 -> 7, 111 -> 8
    Posición: 00 -> 0, 01 -> 1, 10 -> 2, 11 -> 3
Un ejemplo es el siguiente:
    código = 4825
    en bits = 00011011111000111100
        donde el dígito 8 corresponde a los 5 bits siguientes: 01111  
"""

import numpy as np
import random

class AlgoritmoGenetico:
    def __init__(self,codigo):
        self.codigo = codigo
        
    # Generando individuo de forma binaria, primero se genera la posición seleccionando un decimal al azar de una lista 
    # y después se convierte a binario. Posteriormente se genera el dígito directamente en binario al azar y se unen en 
    # en un array ambas partes en forma binaria
        
    def generarIndividuo(self):
        individuo = np.empty
        posiciones = [0,1,2,3]
        for i in range(4):
            posicion = random.choice(posiciones)
            posiciones.remove(posicion)
            if(posicion == 0):
                p1 = np.random.randint(0,1,(1))
                p2 = np.random.randint(0,1,(1))
                posicion = np.append(p1,p2)
                numero = np.random.randint(0,2,(3))
                digito = np.append(posicion,numero)
                individuo = np.append(individuo,digito)
            elif(posicion == 1):
                p1 = np.random.randint(0,1,(1))
                p2 = np.random.randint(1,2,(1))
                posicion = np.append(p1,p2)
                numero = np.random.randint(0,2,(3))
                digito = np.append(posicion,numero)
                individuo = np.append(individuo,digito)
            elif(posicion == 2):
                p1 = np.random.randint(1,2,(1))
                p2 = np.random.randint(0,1,(1))
                posicion = np.append(p1,p2)
                numero = np.random.randint(0,2,(3))
                digito = np.append(posicion,numero)
                individuo = np.append(individuo,digito)
            elif(posicion == 3):
                p1 = np.random.randint(1,2,(1))
                p2 = np.random.randint(1,2,(1))
                posicion = np.append(p1,p2)
                numero = np.random.randint(0,2,(3))
                digito = np.append(posicion,numero)
                individuo = np.append(individuo,digito)
        individuo = np.delete(individuo,0)
        return individuo
    
    # Generado la población que se utiliza en el algoritmo genético dependiendo del número de individuos     

    def generaPoblacion(self,nInd):
        poblacion = []
        for i in range(nInd):
            individuo = self.generarIndividuo()
            poblacion.append(list(individuo))
        return poblacion
        
    
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
        for i in range(4):
            numerosEnBits.append(individuo[i*5:(i+1)*5])
        for d in numerosEnBits:
            posicion = d[0:2] 
            digito = d[2:]
            C.append([self.bitsADigito(digito),self.bitsADigito(posicion)-1])
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
    
    # Calificando al individuo dependiendo de la posición de sus dígitos.

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
        poblacion = self.generaPoblacion(nInd)
        gen = 0
        while(gen<nMaxGen):
            evaluacion = self.evaluaPoblacion(poblacion)
            nuevaPoblacion = self.procesoEvolutivo(poblacion,evaluacion,tam)
            poblacion = nuevaPoblacion
            gen+=1
        mejor,peor = self.buscaMejorPeor(evaluacion)
        mejorCodigo = self.genotipoAFenotipo(poblacion[mejor])     
        return mejorCodigo
    
    
class Juego:
    def __init__(self):
        self.encontrado = False
        self.codigo = self.generarCodigo()
        print("Código original: ",self.codigo,end="\n\n")
        
    # Generando de forma aleatoria el código de 4 dígitos que se va a buscar, donde cada dígito puede ir desde 1 a 8

    def generarCodigo(self):
        codigo = []
        for i in range(4):
            codigo.append(np.random.randint(1,9))    
        return codigo
    
    # Acomodando el dígito ingresado según su posición 
    
    def acomodarDigito(self,digitos):
        numero = [0,0,0,0]
        try:    
            for i in digitos:
                numero[i[1]] = i[0]  # Acomodando digitos en posición
            return numero
        except NameError:
            pass
    
    # Verificando si se encontró el código
        
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
    
    # Inicio del juego, en cada intento buscará encontrar el código con el algoritmo genético
    
    def jugar(self):
        aux = 1
        resultado = []
        while(not self.encontrado):
            print(f"- Intento {aux} -")
            aux+=1
            AG = AlgoritmoGenetico(self.codigo)
            digitos = AG.algoritmoGen(1000,20,1000)
            resultado = self.acomodarDigito(digitos)
            a,b = self.valorarAB(resultado)
            if(a==4 and b==0):
                self.encontrado = True
                print("Código ENCONTRADO!: ",resultado)
            else:
                print("Código no encontrado, mejor resultado: ",resultado,end="\n\n")

            
# Ejecutando el juego         
            
juego = Juego()
juego.jugar()