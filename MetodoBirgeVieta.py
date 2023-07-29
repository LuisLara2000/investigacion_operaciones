import os

def ImprimirMatriz(matrix,longitud):
    for i in range(5):
        for l in range(longitud):
            print("--------------",end="")
        print(" ")
        for j in range(longitud):
            #print(matrix[i][j],end=" ")
            print("|"+'{:>12.6f}'.format(matrix[i][j]),end=" ")
            #print("|",end=" ")
        print("|", end=" ")
        print(" ")
    for l in range(longitud):
        print("--------------", end="")
    print(" ")        
def Entradas():
    valorMaximoPolinomio = 0
    longitud = 0
    valorMaximoPolimonioCorrecto = False
    listaTerminos=[]
    listaTerminos.clear()
    #Validamos la entrada de la cantidad del grado del polinomio 
    while valorMaximoPolimonioCorrecto==False:
        print("Ingrese el grado mayor del polinomio = ",end=" ")
        valorMaximoPolinomio = str(input())
        #Validamos la entrada
        longitud = len(valorMaximoPolinomio)
        # Validamos que cada caracter sea un numero
        valorMaximoPolimonioCorrecto = True
        for i in range(longitud):
            if ord(valorMaximoPolinomio[i]) < 48 or ord(valorMaximoPolinomio[i])>57:
                valorMaximoPolimonioCorrecto = False
        if valorMaximoPolimonioCorrecto == True:
            if int(valorMaximoPolinomio) <= 0:
                valorMaximoPolimonioCorrecto = False

    ValorDeCadaTerminoCorrecto = False
    valorTermino=0
    longitudtermino=0
    unDecimal = False
    #Validamos la entrada de cada valor de cada termino
    for t in range(int(valorMaximoPolinomio)+1):    
        ValorDeCadaTerminoCorrecto = False
        while ValorDeCadaTerminoCorrecto == False:
            ValorDeCadaTerminoCorrecto = True
            #print("El mesaje de x^1 esta mal debe empezar en x^al maximo exponente")
            if t < int(valorMaximoPolinomio):
                print("Valor de x^"+str(int(valorMaximoPolinomio)-t)+"=", end=" ")
            else:
                print("Valor independiente=", end=" ")
            valorTermino = str(input())
            longitudtermino = len(valorTermino)
            unDecimal = False
            for e in range(longitudtermino):     
                if ord(valorTermino[e]) < 48 or ord(valorTermino[e]) > 57:           
                    if unDecimal == True:
                        ValorDeCadaTerminoCorrecto=False
                    elif ord(valorTermino[e]) == 46:
                        unDecimal = True
                    elif ord(valorTermino[e]) != 46 and ord(valorTermino[e]) != 45: 
                        ValorDeCadaTerminoCorrecto = False
                #else:
                #   ValorDeCadaTerminoCorrecto = False
                #    print("letra")
        listaTerminos.append(float(valorTermino))
    return listaTerminos
def ValorInicialCalcular(Opcion,listaDeTerminos,Matrix):
    terminos=[]
    valorInicio = 0
    terminos = listaDeTerminos
    lon = len(terminos)

    if Opcion == 0:
        valorInicio = (terminos[lon-1]*-1)/terminos[lon-2]
    else:
        if Matrix[4][lon-1]!=0:
            valorInicio = Matrix[0][0]-(Matrix[2][lon]/Matrix[4][lon-1])
        else:
            valorInicio = Matrix[0][0]
    return valorInicio
def iteracion(listaDeTerminos,valorInicialParametro):
    terminos=[]
    matriz=[]
    terminos = listaDeTerminos
    iteracionLimite = 10
    operacion = 0
    #limpiamos la matriz en cada iteracion
    matriz.clear()
    #print("longitud"+str(int(len(terminos))))
    #creamos la matriz
    for w in range(5):
        matriz.append([])
        for s in range(int(len(terminos)+1)):
            matriz[w].append(0)

    #ImprimirMatriz(matriz)
    operacion = int(len(terminos))-1
    #Entramos a las iteraciones 
    for i in range(iteracionLimite):
        #ingresamos los datos base en la matriz que utilizaremos para aplicar la formula
        matriz[0][0]=valorInicialParametro
        for e in range(int(len(terminos))):
            matriz[0][e+1]=terminos[e]
        matriz[2][1] = terminos[0]
        matriz[4][1]=terminos[0]
        #ImprimirMatriz(matriz)
        for u in range(2):
            for l in range(operacion):
                matriz[1+(2*u)][2+l] = matriz[0][0]*matriz[2+(u*2)][1+l]
                #print(matriz[1+(2*u)][2+l])
                #print(matriz[u*2][2+l])
                #print(matriz[1+(u*2)][2+l])
                matriz[2+(2*u)][2+l] = matriz[u*2][2+l]+matriz[1+(u*2)][2+l]
            #ImprimirMatriz(matriz)
            operacion=operacion-1
        
    #
    return matriz
def divisonSintetica(listaTerminos,raiz):
    polinomioReducido = []
    matrizSintetica = []
    #creamos una matriz para mostrar la divison
    for c in range(3):
        matrizSintetica.append([])
        for j in range(len(listaTerminos)+1):
            matrizSintetica[c].append(0)
    #-----------------------------------------
    #inicio la matriz
    for k in range(1,len(listaTerminos)+1):
        matrizSintetica[0][k] = listaTerminos[k-1]
    # escribo el valor de la raiz porque le ciclo se lo brinca 
    matrizSintetica[0][0] = raiz
    matrizSintetica[2][1]= listaTerminos[0]
    for p in range(len(listaTerminos)-1):
        matrizSintetica[1][2+p] = matrizSintetica[2][1+p]*matrizSintetica[0][0]
        matrizSintetica[2][2+p] = matrizSintetica[1][2+p]+matrizSintetica[0][2+p]
    #print(matrizSintetica)
    # mensaje --------------------------------
    print(" ")
    print("Aplicamos divison sintetica al polinomio ",end="")
    for o in range(len(listaTerminos)-1):
        #'{:.6f}'.format(str(listaTerminos[o]))
        print('{:.6f}'.format(listaTerminos[o])+"x^"+str(int(len(listaTerminos))-1-o),end="")
        if listaTerminos[o+1] >+ 0:
            print(" +",end="")
    #'{:.6f}'.format(listaTerminos[int(len(listaTerminos))-1])
    print('{:.6f}'.format(listaTerminos[int(len(listaTerminos))-1]))
    print(" ")
    for i in range(3):
        for t in range(len(listaTerminos)+1):
            print('{:>12.6f}'.format(matrizSintetica[i][t]), end=" ")
            if t == 0 and i!=2:
                print("|",end="")
        #print("|", end=" ")
        print(" ")
        if i == 1:
            print("             |", end="")
            for p in range(len(listaTerminos)+1):
               print("____________", end="")
            print(" ")
        
    # mensaje --------------------------------

    for e in range(len(listaTerminos)-1):
        polinomioReducido.append(matrizSintetica[2][1+e])
    #print(polinomioReducido)
    return polinomioReducido

def Principal():
    terminos=[]
    terminosTemporal = []
    matrizOperaciones = []
    raices = []
    tem=[]
    valorInicial = 0
    seguir = 0
    Error = 100   

    while seguir == 0:

        valorInicial = 0
        terminos = Entradas()
        CantidadSoluciones = len(terminos)-1
        x = 0 # mensaje
        nosolucion = 0
        Error = 100

        for y in range(CantidadSoluciones):
            raices.append([])

        for h in range(CantidadSoluciones):# se repite la cantidad de soluciones que tiene el polinomio
           
            valorInicial = ValorInicialCalcular(0, terminos, matrizOperaciones)

            while Error > 0.001:# valor temporal lo hare mas pequeño al final
                #print("valor incial:"+str(valorInicial))
                matrizOperaciones = iteracion(terminos,valorInicial)  
                Error = matrizOperaciones[2][len(terminos)]
                #print("ERROR:"+str(Error))
                # -- mensajes----------------------------------------------------------
                x=x+1
                print(" ")
                print("________________________________________________")
                print("| ITERACION "+str(x)+"                                  |")
                print("|______________________________________________|")
                print("| RAIZ | "+'{:>12.6f}'.format(valorInicial), end=" ")
                print("| ERROR |   "+'{:>12.6f}'.format(Error), end=" ")
                print("|")
                print("|______________________________________________|")
                print(" ")
                ImprimirMatriz(matrizOperaciones,len(terminos)+1)
                # -- mensajes----------------------------------------------------------
                valorInicial = ValorInicialCalcular(1, terminos, matrizOperaciones)

                # despues de 50 interaciones, concluimos que la solucion es compleja 
                if x>50:
                    nosolucion = 1
                    Error = 0
                    os.system("cls")
                
                #f=0
                #f = input()
            x = 0  # mensaje

            if nosolucion != 1:
                print(" ")
                print("RAIZ x"+str(h)+" = "+str(valorInicial))
                raices[h]=valorInicial
                terminosTemporal = terminos
                terminos.clear
                Error = 100
                if h != CantidadSoluciones-1:
                    terminos = divisonSintetica(terminosTemporal,valorInicial)
            else:
                h = CantidadSoluciones+5
   
        if nosolucion != 1:
            print("")
            print("La solucion del polinomio es ",end="")
            for t in range(CantidadSoluciones):
                print("(x",end="")
                if (raices[t]*-1)>=0:
                    print("+",end="")
                print('{:.6f}'.format(float(raices[t])*-1)+")",end="")
        else:
            print("El polinomio tiene soluciones complejas")
            if len(raices)>0:
                print("Raices encontradas: ",end="")
                print(raices)
        
        for p in range(CantidadSoluciones):
            raices.pop(0)

        for l in range(len(terminos)):
            terminos.pop(0)

        print(" ")
        print(" ")
        print("¿DESEA INGRESAR OTRO POLINOMIO?") 

        seguir = int(input())
        os.system("cls")
        if seguir != 0:
            print("FIN DEL PROGRAMA XD")

Principal()
