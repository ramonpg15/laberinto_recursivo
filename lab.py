""" Para cargar el archivo """
import os
from time import sleep, time
import time

def cargar_archivo(nombre_archivo):
    archivo = open(nombre_archivo)
    laberinto = archivo.read()
    archivo.close()
    return laberinto

""" Para convertir el archivo en matriz """
def convertir_laberinto(laberinto):
    laberinto_convertido = []
    lineas = laberinto.splitlines()
    for linea in lineas:
        laberinto_convertido.append(list(linea))
    return laberinto_convertido

""" Imprime el laberinto """
def imprimir_laberinot(laberinto):
    for fila in laberinto:
        for i in fila:
            print(i,end='')
        print()
""" Buscar la posicion inicial, marcada como una 'E' """
def posicion_inicial(laberinto):
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if laberinto[fila][columna]=='E':
                return fila,columna
   
#from time import sleep

def posicion_valida(laberinto, pos_fila, pos_columna):
    if pos_fila < 0 or pos_columna < 0:
        return False
    if pos_fila >= len(laberinto) or pos_columna >= len(laberinto[0]):
        return False
    if laberinto[pos_fila][pos_columna] in ' @':
        return True
    return False
    
def buscar_salida(laberinto,inicio):
    pila=[]
    conta=0
    pila.append(inicio)
    while len(pila) > 0:
        conta+=1
        pos_fila, pos_columna = pila.pop()
        if laberinto[pos_fila][pos_columna] == '@':
            print('Meta')
            return True
        if laberinto[pos_fila][pos_columna]=='v':
            
            #return False
            continue
        laberinto[pos_fila][pos_columna]='.'
        #imprimir_laberinot(laberinto)
        if posicion_valida(laberinto,pos_fila+1, pos_columna):
            pila.append((pos_fila+1,pos_columna))
            #contador +=1 
        if posicion_valida(laberinto,pos_fila,pos_columna-1):
            pila.append((pos_fila,pos_columna-1))
            #contador +=1 
        if posicion_valida(laberinto,pos_fila,pos_columna+1):
            pila.append((pos_fila,pos_columna+1))
            #contador +=1 
        if posicion_valida(laberinto, pos_fila-1,pos_columna):
            pila.append((pos_fila-1,pos_columna))
            #contador +=1 
        print('Pila',pila)
        print(len(pila))
        print('\n')
        print('conta',conta)
        time.sleep(0.05)
        os.system('clear')
        imprimir_laberinot(laberinto)
    return False

  
    
laberinto = cargar_archivo('ejemplo2.txt')
laberinto = convertir_laberinto(laberinto)
imprimir_laberinot(laberinto)
inicio = posicion_inicial(laberinto)
print(inicio)
print(buscar_salida(laberinto, inicio)) 