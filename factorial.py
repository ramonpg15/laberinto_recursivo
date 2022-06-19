
""" def calcular_factorial(numero):
    if numero > 1:
        numero = numero * calcular_factorial(numero-1)
    return numero
        
numero = int(input('De que numero quieres sacar el factorial? '))
res= calcular_factorial(numero)
print(res)
 """
def hola(num):
    if num>1:
        num = hola(num-1)
    
    return num
hola(8)