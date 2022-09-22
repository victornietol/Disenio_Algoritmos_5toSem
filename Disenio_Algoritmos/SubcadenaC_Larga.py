def encontrarM(matriz):
    mayor = 0
    ren = 0
    col = 0
    for e in matriz:
        for j in e:
            if(j > mayor):
                col_f = col
                mayor = j
            col +=1
        col = 0
        ren +=1
    return col_f,mayor     

def encontrarSub(cadena,mayor,col):
    subcadena = cadena[col-(mayor-1):col+1]
    return subcadena

def SubML(cadena1, cadena2):
    n = len(cadena1)
    m = len(cadena2)
    aux_e = 0 # columnas
    aux_i = 0 # renglones
    matriz = [[0 for x in range(n)] for j in range(m)]
    for e in cadena2:
        for i in cadena1:
            if(e==i):
                matriz[aux_e][aux_i] = 1
                if (aux_e != 0) and (aux_i != 0):
                    matriz[aux_e][aux_i] += matriz[aux_e-1][aux_i-1]
            elif(e!=i):
                pass
            aux_i +=1 
        aux_e +=1 
        aux_i = 0
    col,mayor = (encontrarM(matriz))
    subcadena = encontrarSub(cadena1,mayor,col)
    return subcadena


#cadena1 = 'anrieofesaragongrethf'
#cadena2 = 'esfsrfefesaragonvxn'

cadena1 = 'aaaaaaaxsxpruebakjiei'
cadena2 = 'egfdsgerggreaaaaaaapruebadiore'
print(SubML(cadena1,cadena2))