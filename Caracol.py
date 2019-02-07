def getArchivo():
    return "Matriz.txt"

def leer_archivo(txt):
    return [[int(x) for x in y] for y in [x.split(" ") for x in [y.strip("\n") for y in open(txt).readlines()]]]

print (leer_archivo(getArchivo()))

def tamaño(matriz):
    return len(matriz[0])

def recorrido(direccion, matriz, i, j):

    print(matriz[i][j])
    
    if(direccion == 1):
##        print(matriz)
##        print("i:" , i , " j:" , j)
        if((j+1) == len(matriz)):
##            print(matriz)
            recorrido(2, getArriba(matriz), (i), (j)) 
        recorrido(direccion, matriz, (i), (j+1)) ##DERECHA
        
    elif(direccion == 2):
##        print(matriz)
##        print("i:" , i , " j:" , j)
        if((i+1) == len(matriz)):
##            print(matriz)
            recorrido(3, getDerecha(matriz), (i), (j-1)) 
        recorrido(direccion, matriz, (i+1), (j)) ##ABAJO
       
    elif(direccion == 3):
##        print(matriz)
##        print("i:" , i , " j:" , j)
        if( j == 0):
##            print(matriz)
            recorrido(4, getAbajo(matriz, len(matriz)), (i-1), (j)) 
        recorrido(direccion, matriz, (i), (j-1)) ##IZQUIERDA

    elif(direccion == 4):
##        print("**i:" , i , " j:" , j)
        if( i == 0):
##            print(matriz)
            recorrido(1, getIzquierda(matriz), (i), (j+1)) 
        recorrido(direccion, matriz, (i-1), (j)) ##ARRIBA

def getArriba(matriz):
    return matriz[1:]

def getDerecha(matriz):
    [x.pop() for x in matriz]
    return matriz

def getAbajo(matriz, tamaño):
    print ("***", tamaño)
    return matriz[:(tamaño-1)]

def getIzquierda(matriz):
    [x.pop(0) for x in matriz]
    return matriz

print(recorrido(1, leer_archivo(getArchivo()), 0 , 0))
    
