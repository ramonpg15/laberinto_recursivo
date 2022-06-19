import os
import time
from traceback import print_last
ubicacion = []
contPasos=0
pila=[]
def inicio():
    meta = []
    sinFin = True
    nombre_archivo = input('Ingresa el nombre del archivo a resolver: ')
    laberinto = leer(nombre_archivo)
    for fila in range(0,len(laberinto)):
        for columna in range(0,len(laberinto[fila])):
            if laberinto[fila][columna] == 'E':
                ubicacion = [fila,columna]
                print(f'Ubicacion inicial {ubicacion}')
            elif laberinto[fila][columna] == '@':
                meta = [fila,columna]
                sinFin = False
    if len(ubicacion) == 0:
        raise Exception('No se encontro celda de inicio,verifica tu archivo .txt')
    if sinFin:
        raise Exception('Laberinto sin solucion ')
    print('Laberinto original:\n')
    imprimir_laberinto(laberinto)
    
    def opcion_grafica():
        global contPasos
        inicio = time.time()
        solucion(laberinto,ubicacion[0],ubicacion[1])
        fin = time.time()
        res = fin - inicio
        print(f'Meta encontrada en: {meta}')
        print(f'Tardo {res} segundos')
        print(f'Meta encontrada en: {contPasos}')
        #globals()['contPasos'] = 0
        contPasos=0
        salir()
        
    def opcion_automatica():
        global contPasos
        inicio = time.time()
        solucion_g(laberinto,ubicacion[0],ubicacion[1])
        fin = time.time()
        imprimir_laberinto(laberinto)
        print(f'Solucion encontrada en: {meta} con un tiempo de {fin-inicio} segundos con un total de {contPasos} pasos')
        #globals()['contPasos'] = 0
        contPasos=0
        salir()

    menu()
    pregunta = True
    while(pregunta):
        opcion = int(input('Teclea la opciòn deseada: '))
        if opcion == 1:
            opcion_grafica()
            pregunta = False
        elif opcion == 2:
            opcion_automatica()       
            pregunta = False
        elif opcion == 3:
            print('Hasta luego')
            pregunta = False
        else:
            print('Opción incorrecta')
            pregunta = True 
   
def leer(nombre_archivo):
    archivo = open(nombre_archivo,'r')
    laberinto = [list(fila) for fila in archivo.read().splitlines()]
    archivo.close()
    return laberinto
 
 

def imprimir_laberinto(laberinto):
    print('\n'.join(''.join(fila) for fila in laberinto))
 

def solucion(laberinto,fila,columna):
    global contPasos
    #contador = 0
    #global pila
    os.system('clear')
    imprimir_laberinto(laberinto)
    print('\n')
    
    if laberinto[fila][columna] in (' ','E'): 
        laberinto[fila][columna] = '*'
        time.sleep(.005)
        if(solucion(laberinto,fila,columna+1) or solucion(laberinto,fila+1,columna) or 
           solucion(laberinto,fila,columna-1) or solucion(laberinto,fila-1,columna)):
            laberinto[fila][columna] = 'c'
     #       pila.append([fila,columna])
            contPasos+=1
     #       print[pila]
            return True        
    elif laberinto[fila][columna]=='@':
        return True
    
    return False 
    
       

def solucion_g(laberinto,fila,columna):
    pila=[]
    global contPasos
    os.system('clear')
    print('Espere...')
    print('\n')
    if laberinto[fila][columna] in (' ','E'): 
        #contador+=1
        laberinto[fila][columna] = 'o'
        pila = laberinto[fila][columna]
        #contador+=1
        if(solucion_g(laberinto,fila,columna+1) or solucion_g(laberinto,fila+1,columna) or 
           solucion_g(laberinto,fila,columna-1) or solucion_g(laberinto,fila-1,columna)):
            laberinto[fila][columna] = 'c'
            contPasos = contPasos +1
            return True
        print('Pila',pila)
    elif laberinto[fila][columna]=='@':
        return True
    return False
    
 

def menu():
    print('\n')
    print('Selecciona una opcion de las siguientes: ')
    print('1) Opción grafica')
    print('2) Opcion automatica')
    print('3) Salir')
    
    
    
def salir():
    res = input('Deseas salir ? (Y/N): ')
    res= res.lower()
    if res == 'n':
        inicio()
    return False

    
inicio()