import os

def entradas():
    tablaDePuntos = []
    tablaDePuntosTemporal = []
    puntosX=[]
    puntosY=[]
    # Validamos la entrada de la maxima cantidad de puntos
    cantidadDePuntosMaxima = False
    while cantidadDePuntosMaxima == False:
        print("\033[;36m"+"INGRESE LA CANTIDAD DE PUNTOS = "+'\033[0;m', end=" ")
        cantidadDePuntos = str(input())
        #Validamos la entrada
        longitud = len(cantidadDePuntos)
        # Validamos que cada caracter sea un numero
        cantidadDePuntosMaxima = True
        for i in range(longitud):
            if ord(cantidadDePuntos[i]) < 48 or ord(cantidadDePuntos[i]) > 57:
                cantidadDePuntosMaxima = False
        if cantidadDePuntosMaxima == True:
            if int(cantidadDePuntos) <= 1:
                cantidadDePuntosMaxima = False
    # Generamos la tabla
    for p in range(int(cantidadDePuntos)+1):
        tablaDePuntos.append([" "])
        for q in range(1):
            tablaDePuntos[p].append(" ")
    # Inicializamos la tabla
    tablaDePuntos[0][0] = "  X  "
    tablaDePuntos[0][1] = "  Y  "
    primera = 0
    # Validamos la entrada de cada valor de cada termino
    for t in range(1,int(cantidadDePuntos)+1):
        ValorDeCadaTerminoCorrecto = False
        print("\033[;36m"+"Punto #"+str(t)+'\033[0;m')
        for l in range(2):
            if l == 0:
                print("x =", end=" ")
            else:
                print("y =", end=" ")
            ValorDeCadaTerminoCorrecto = False

            while ValorDeCadaTerminoCorrecto == False:
                ValorDeCadaTerminoCorrecto = True
                valorTermino = str(input())
                longitudtermino = len(valorTermino)
                unDecimal = False
                for e in range(longitudtermino):
                    if ord(valorTermino[e]) < 48 or ord(valorTermino[e]) > 57:
                        if unDecimal == True:
                            ValorDeCadaTerminoCorrecto = False
                        elif ord(valorTermino[e]) == 46:
                            unDecimal = True
                        elif ord(valorTermino[e]) != 46 and ord(valorTermino[e]) != 45:
                            ValorDeCadaTerminoCorrecto = False 
                # validar que el numero no se haya repetido tanto x como y
                if primera > 1 and ValorDeCadaTerminoCorrecto == True:
                    if l==0:# ingresar x
                        if float(valorTermino) in puntosX:
                            ValorDeCadaTerminoCorrecto = False
                            print("x =",end=" ")
                        else:
                            puntosX.append(float(valorTermino))          
                    else:
                        if float(valorTermino) in puntosY:
                            ValorDeCadaTerminoCorrecto = False
                            print("y =", end=" ")
                        else:
                            puntosY.append(float(valorTermino))
                else: 
                    if  ValorDeCadaTerminoCorrecto == True:
                        primera += 1
                        if l == 0: 
                            puntosX.append(float(valorTermino))
                        else:
                            puntosY.append(float(valorTermino))
                    else:
                        if l == 0:  
                            print("x =", end=" ")
                        else:
                            print("y =", end=" ")
    # Ordenamos los puntos
    puntosXTemporal = []
    puntosYTemporal = []
    maximo = 0
    minimo = 0
    maximo = max(puntosX)

    for p in range(len(puntosX)):
        maximo = max(puntosX)
        minimo = min(puntosX)
        for u in range(len(puntosX)):
            if puntosX[u] == minimo:
                puntosXTemporal.append(puntosX[u])
                puntosYTemporal.append(puntosY[u])
                puntosX[u] = maximo+10

    puntosX = puntosXTemporal
    puntosY = puntosYTemporal
    
    for t in range(1, int(cantidadDePuntos)+1):
        for l in range(2):
            if l == 0:
                tablaDePuntos[t][l] = float(puntosX[t-1])
            else:
                tablaDePuntos[t][l] = float(puntosY[t-1])
    return tablaDePuntos
def puntoEvaluar():
    p = 0    
    print("\033[;36m"+"PUNTO A EVALUAR: "+'\033[0;m', end="")
    #p = float(input())
    valorTermino = 0
    ValorDeCadaTerminoCorrecto = False
    while ValorDeCadaTerminoCorrecto == False:
        ValorDeCadaTerminoCorrecto = True
        valorTermino = str(input())
        longitudtermino = len(valorTermino)
        unDecimal = False
        for e in range(longitudtermino):
            if ord(valorTermino[e]) < 48 or ord(valorTermino[e]) > 57:
                if unDecimal == True:
                    ValorDeCadaTerminoCorrecto = False
                elif ord(valorTermino[e]) == 46:
                    unDecimal = True
                elif ord(valorTermino[e]) != 46 and ord(valorTermino[e]) != 45:
                    ValorDeCadaTerminoCorrecto = False
        if ValorDeCadaTerminoCorrecto == False:
            print("\033[;36m"+"PUNTO A EVALUAR: "+'\033[0;m', end="")
    p = float(valorTermino)
    os.system("cls")
    return p
def imprimirTabla(tabla,puntoo):
    print("\033[;36m"+"PUNTOS INGRESADOS"+'\033[0;m')
    columnas = len(tabla)
    cadenaTemporal = " "
    cadenaimprimir = " "
    for k in range(2):
        for t in range(columnas):
            if k == 0:
                if t > 0:
                    cadenaTemporal = str(tabla[t][k])
                    cadenaimprimir = cadenaTemporal.center(10," ")
                    print("\033[0;37;44m"+" "+str(cadenaimprimir)+" "+'\033[0;m', end=" ")
                else:
                    print("\033[0;37;44m"+" "+str(tabla[t][k])+" "+'\033[0;m', end=" ")
            else:
                if t > 0:
                    cadenaTemporal = str(tabla[t][k])
                    cadenaimprimir = cadenaTemporal.center(10, " ")
                    print("\033[0;30;47m"+" "+str(cadenaimprimir)+" "+'\033[0;m', end=" ")
                else:
                    print("\033[0;30;47m"+" "+str(tabla[t][k])+" "+'\033[0;m', end=" ")
        if k == 0:
            print("    ",end=" ")
            cadenaTemporal = "Punto"
            cadenaimprimir = cadenaTemporal.center(10, " ")
            print("\033[0;37;41m"+" "+str(cadenaimprimir)+" "+'\033[0;m', end=" ")
            print("\033[0;30;40m"+"s"+'\033[0;m', end=" ")
        else:
            print("    ", end=" ")
            cadenaTemporal = str(puntoo)
            cadenaimprimir = cadenaTemporal.center(10, " ")
            print("\033[0;30;47m"+" "+str(cadenaimprimir)+" "+'\033[0;m', end=" ")
            print("\033[0;30;40m"+"s"+'\033[0;m', end=" ")
        print(" ")
    print(" ")
def formaBase(tabla):
    longitud = len(tabla)-1
    matrizFormaBase = []
    forma = []
    margen = 2

    for i in range(longitud):
        matrizFormaBase.append([])
        for j in range(1,longitud+1):
            if j < margen:
                matrizFormaBase[i].append("x")                
                matrizFormaBase[i].append(str(float(tabla[j][0])*-1))
            else:
                matrizFormaBase[i].append("-")
                matrizFormaBase[i].append("-")
        margen += 1
  
    lon2 = len(matrizFormaBase)
    margen2 = 2
    print("\033[;36m"+"FORMA BASE DEL SISTEMA"+'\033[0;m')
    print("f(x) = C0 + ",end="")
    forma.append("C0")
    for i in range(lon2-1):
        print("C"+str(i+1), end="")
        print("(",end="")
        forma.append("C"+str(i+1))
        forma.append("(")
        for x in range(lon2*2):
            if x < margen2:
                if x % 2 != 1 and x>=1:
                    print(")",end="")
                    forma.append(")")
                if x % 2 == 0 and x >= 2:
                    print("(", end="")
                    forma.append("(")
                if str(matrizFormaBase[i][x]) != "x" and str(matrizFormaBase[i][x]) != "-":
                    if float(matrizFormaBase[i][x]) > 0:
                        print("+",end="")
                print(matrizFormaBase[i][x],end="")
                forma.append(str(matrizFormaBase[i][x]))
                    
        print(")", end="")
        forma.append(")")
        if i != lon2-2:
            print(" + ",end="")
        margen2+=2
    print("")
    return forma
def generarMatriz(listaFormaBase, tabla):
    matrizCoeficientes = []
    print(" ")
    print("\033[;36m"+"RESOLVEMOS EL SIGUIENTE SISTEMA"+'\033[0;m')
    longitud = len(tabla)-1
    loon = len(listaFormaBase)
    for k in range(longitud):
        matrizCoeficientes.append([1])
        for q in range(longitud):
            matrizCoeficientes[k].append(1)

    for i in range(longitud):
        numero = 1
        sustituirX = tabla[i+1][0]
        matrizCoeficientes[i][0] = 1

        j = 0
        for l in range(loon):
            if listaFormaBase[l] == str("C"+str(numero)) :
                print(" + ",end="")
                numero+=1 
                j+=1
            if listaFormaBase[l] != "x":
                print(listaFormaBase[l],end="")
            else:
                print(sustituirX, end="")
                matrizCoeficientes[i][j] *= float(sustituirX) + float(listaFormaBase[l+1])
        j += 1
        matrizCoeficientes[i][j] = float(tabla[i+1][1])
        print(" = "+str(tabla[i+1][1]), end="")
        print(" ")
    print(" ")
    print("\033[;36m"+"MATRIZ INICIAL"+'\033[0;m')

    pp = len(matrizCoeficientes)
    for k in range(pp):
        for l in range(pp+1):
            print('{:>10.4f}'.format(matrizCoeficientes[k][l]), end="")
            if l == pp-1:
                print(" |",end="")
        print("")

    return matrizCoeficientes
def resolverMatriz(matrizCoeficientes):
    # metodo de gauss simple
    longitud = len(matrizCoeficientes)
    veces = longitud
    inicio =0
    for i in range(longitud-1):#veces que resulve columnas
        for x in range(i,veces-1):#operaciones 
            matrizCoeficientes[x+1][longitud] = matrizCoeficientes[x+1][longitud]-matrizCoeficientes[x+1][i]*(matrizCoeficientes[i][longitud]/matrizCoeficientes[i][i])
            matrizCoeficientes[x+1][i] = matrizCoeficientes[x+1][i]-matrizCoeficientes[x+1][i]*(matrizCoeficientes[i][i]/matrizCoeficientes[i][i])         
        inicio+=1
        matrizCoeficientes[i][longitud] = matrizCoeficientes[i][longitud]/matrizCoeficientes[i][i]
        matrizCoeficientes[i][i] = matrizCoeficientes[i][i]/matrizCoeficientes[i][i]
    matrizCoeficientes[longitud-1][longitud] = matrizCoeficientes[longitud-1][longitud]/matrizCoeficientes[longitud-1][longitud-1] 
    matrizCoeficientes[longitud-1][longitud-1] = matrizCoeficientes[longitud-1][longitud-1]/matrizCoeficientes[longitud-1][longitud-1]
    print(" ")
    print("\033[;36m"+"MATRIZ RESUELTA"+'\033[0;m')
    #Matriz resuelta  
    pp = len(matrizCoeficientes)
    for k in range(pp):
        for l in range(pp+1):
            print('{:>10.4f}'.format(matrizCoeficientes[k][l]), end="")
            if l == pp-1:
                print(" |", end="")
        print("")
    return matrizCoeficientes
def evaluar(puntoE, matrizResuelta, listaFormaBase):
    print(" ")
    print("\033[;36m"+"EVALUAMOS EN LA FORMA BASE"+'\033[0;m')
    longitud = len(listaFormaBase)
    c = 0
    signoMas = 1
    multiplicador = 1
    resultado = 0
    listaResultado = []
    print("f("+str(puntoE)+") = ",end=" ")
    for i in range(longitud):
        if str(listaFormaBase[i]) == "x":
            print(str(puntoE),end="")
            # lo sumo porque ya se invirtio el signo anteriormente
            listaResultado.append(str(puntoE+float(listaFormaBase[i+1])))
        elif str(listaFormaBase[i]) == "C"+str(c):
            print(matrizResuelta[c][len(matrizResuelta)], end="")
            if i != 0:
                listaResultado.append(str("#"))
            listaResultado.append(str(matrizResuelta[c][len(matrizResuelta)]))
            c += 1
        else:
            if str(listaFormaBase[i]) == "(" or str(listaFormaBase[i]) == ")":
                print(listaFormaBase[i], end="")
            else:
                
                if float(listaFormaBase[i]) < 0:
                    print(listaFormaBase[i], end="")
                else:
                    print("+"+str(listaFormaBase[i]), end="")
        signoMas-=1
        if signoMas<=0 and c != len(matrizResuelta):
            signoMas = (4*multiplicador)+1
            multiplicador +=1
            print(" + ",end="")
    resultadoTemporal = 1
    margen = 0
    #sumar
    for t in range(len(listaResultado)):
        if str(listaResultado[t]) != "#":
            resultadoTemporal *= float(listaResultado[t])
        if str(listaResultado[t]) == "#" or t == len(listaResultado)-1:
            resultado += resultadoTemporal
            resultadoTemporal = 1
    print(" ")
    print(" ")
    print("\033[;36m"+"RESULTADO"+'\033[0;m')
    print("\033[;33m"+"f("+str(puntoE)+") = "+str(resultado)+'\033[0;m')
    
def principal():
    punto = 0
    tablaPuntos = []
    listaFormaBase = []
    matrizResolver=[]
    respuesta = 1
    respuestatem = 0
    mal = 0
    continuar = 0
    os.system("cls")
    while continuar == 0:      
        if respuesta != 0:
            tablaPuntos = entradas()
            punto = puntoEvaluar()
            imprimirTabla(tablaPuntos,punto)
            listaFormaBase = formaBase(tablaPuntos)
            matrizResolver = generarMatriz(listaFormaBase, tablaPuntos)
            resolverMatriz(matrizResolver)
            evaluar(punto,  matrizResolver, listaFormaBase)
        else:
            imprimirTabla(tablaPuntos, punto)
            punto = puntoEvaluar()
            os.system("cls")
            imprimirTabla(tablaPuntos, punto)
            evaluar(punto,  matrizResolver, listaFormaBase)
        respuesta = 0
        respuestatem = 0
        mal = 0
        print(" ")
        print("\033[;36m"+"¿DESEA CONSULTAR OTRO PUNTO?"+'\033[0;m',end=" ")
        print("\033[;37m"+" SI=>0"+'\033[0;m',end=" ")
        print("\033[;31m"+" NO=>1"+'\033[0;m')
        while mal == 0:
            respuestatem = str(input())   
            lonnn = len(respuestatem)
            if lonnn == 1:
                if ord(respuestatem) == 48 or ord(respuestatem) == 49:
                    if ord(respuestatem) == 48:
                        os.system("cls")
                    mal = 1
                    respuesta = int(respuestatem)                   
            else:
                mal = 0
        if respuesta != 0:
            mal = 0
            respuestatem = 0
            print(" ")
            print("\033[;36m"+"¿DESEA INGRESAR NUEVOS PUNTOS?"+'\033[0;m', end=" ")
            print("\033[;37m"+" SI=>0"+'\033[0;m', end=" ")
            print("\033[;31m"+" NO=>1"+'\033[0;m')
            while mal == 0:
                respuestatem = str(input())
                lonnn = len(respuestatem)
                if lonnn == 1:
                    if ord(respuestatem) == 48 or ord(respuestatem) == 49:
                        mal = 1
                        continuar = int(respuestatem)
                        os.system("cls")
                else:
                    mal = 0

  
principal()
