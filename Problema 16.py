"""
Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y (distintos a cero).
Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)
"""

def imprimir_cuadrante(x, y): # Funcion que indica en que cuadrante se encuentra la coordenada
    if x > 0 and y > 0:
        print("La coordenada se encuentra en el primer cuadrante.")
    elif x < 0 and y > 0:
        print("La coordenada se encuentra en el segundo cuadrante.")
    elif x < 0 and y < 0:
        print("La coordenada se encuentra en el tercer cuadrante.")
    else:
        print("La coordenada se encuentra en el cuarto cuadrante.")

#########################   Main    ################################

x = int(input("Ingrese la coordenada x: "))
y = int(input("Ingrese la coordenada y: "))

imprimir_cuadrante(x, y)