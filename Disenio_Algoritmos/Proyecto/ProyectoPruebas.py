import numpy as np

class juego:
    codigo=[]
    solucionado=False
    def __init__(self):
        self.codigo=[]
        self.solucionado=False
        for i in range(4):
            self.codigo.append(np.random.randint(1,9))
    def intento(self,Lista):
        a=0   # a) Dígitos en posición correcta
        b=0   # b) Dígitos en posición incorrecta
        for i,c in zip(Lista,self.codigo):
            if(i==c):
                a+=1
            else:
                if(i in self.codigo):
                    b+=1
        if(a==4):
            self.solucionado=True
            print("Encontrado")
        print("Lista: ",Lista)
        print("self.codigo: ",self.codigo)            
        return a,b

def jugar():
    aux=0
    j1=juego()
    while(not j1.solucionado):
        aux+=1
        lista=[]
        print("Intento: ",aux)
        lista.append(int(input("Ingrese: ")))
        lista.append(int(input("Ingrese: ")))
        lista.append(int(input("Ingrese: ")))
        lista.append(int(input("Ingrese: ")))
        print(j1.intento(lista))
        print()
        

jugar()