"""
Se ingresa por teclado un valor entero, mostrar una leyenda que indique 
si el número es positivo, negativo o nulo (es decir cero)
"""

def mostrar_tipo(entero): # funcion que indica si un numero es positivo, negativo o nulo
    if entero == 0:
        print("El numero es nulo.")
    elif entero < 0:
        print("El numero es negativo.")
    else:
        print("El numero es positivo")

#########################   Main    ################################

entero = int(input("Ingrese un numero: "))

mostrar_tipo(entero)