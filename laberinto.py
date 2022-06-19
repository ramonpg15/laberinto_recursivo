
        
laberinto = [
        ['#','#','#','#','#','#','#','E','#','#','#','#','#','#','#','#','#','#','#'],
        ['#',' ',' ',' ',' ',' ','#',' ','#','#','#',' ',' ',' ',' ',' ',' ',' ','#'],
        ['#',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ','#','#','#','#','#',' ','#'],
        ['#',' ','#',' ','#',' ',' ',' ','#','#','#','#','#','#','#','#','#',' ','#'],
        ['#',' ','#','#','#','#','#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
        ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#',' ','#','#','#','#',' ','#'],
        ['#','#','#','#','#','#',' ','#','#','#','#',' ',' ',' ',' ',' ',' ',' ','#'],
        ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#',' ','#','#','#','#'],
        ['#',' ','#','#','#','#','#','#','#','#','#','#','#','#',' ','#','#','#','#'],
        ['#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
        ['#',' ','#','#','#','#','#','#','#',' ','#','#','#','#','#','#','#',' ','#'],
        ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#'],
        ['#',' ','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
        ['#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
        ['#',' ','#',' ','#','#','#','#','#','#','#',' ','#','#','#','#','#',' ','#'],
        ['#',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ','#','#','#','#','#',' ','#'],
        ['#',' ','#',' ','#','#','#','#','#',' ','#',' ','#',' ',' ',' ',' ',' ','#'],
        ['#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ','#',' ','#',' ','#'],
        ['#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#'],
        ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','@'],
        ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
] 


contador=0
cadena=[]  

"""            
def imprime_laberinto(laberinto):
    for x in range(21):
        for y in range(19):
            print(laberinto[x][y],end=' ')
        print()
       """

""" def buscar_salida(x,y,laberinto):
    if laberinto[x][y]=='@':
        return True
    if laberinto[x][y]=='#' or laberinto[x][y]=='*':
        return False
    laberinto[x][y]='*'
    imprime_laberinto()
    camino = False
    camino=buscar_salida(x,y+1)
    if camino:
        return True
    camino=buscar_salida(x-1,y)
    if camino:
        return True
    camino=buscar_salida(x,y-1)
    if camino:
        return True
    camino=buscar_salida(x+1,y)
    if camino:
        return True
    laberinto[x][y]=' '
    imprime_laberinto()
    return False
             """
"""             
def main():
    pass
main() """
    
    
""" 
"""
def inicio():
    menu()
    pregunta = True
    #opcion= None
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


def menu():
    print('Selecciona una opcion de las siguientes: ')
    print('1) Opción grafica')
    print('2) Opcion automatica')
    print('3) Salir')


def opcion_grafica():
    print('Desde grafica')
    with open('ejemplo.txt') as archivo:
        leer = archivo.read().split('\n')
        print(leer)
    for i in range(0,len(leer)):
        cad = [i for i in leer[contador]]
        contador = contador+1
        cadena.append(cad)
def imprime_laberinto(cadena):
    for j in cadena:
        print(''.join(j))
        
    """ matriz = list(leer)
    print(len(matriz)) """
    #imprime_laberinto(matriz)
  
    
""" def imprime_laberinto(matriz):
    for x in range(21):
        for y in range(19):
            print(matriz[x][y])
        print() """
 

def opcion_automatica():
    print('Desde automatica')


inicio()
