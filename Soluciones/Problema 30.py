"""
Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante.
Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.
"""

def identificar_cuadrante(x, y): # Funcion que indica en que cuadrante se encuentra la coordenada
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

#########################   Main    ################################

cantidad = int(input("Ingresar la cantidad de puntos a procesar: "))

primer = 0
segundo = 0
tercer = 0
cuarto = 0

for x in range(cantidad):
    x = int(input("Ingrese la coordenada x: "))
    y = int(input("Ingrese la coordenada y: "))
    
    if identificar_cuadrante(x, y) == 1:
        primer += 1
    elif identificar_cuadrante(x, y) == 2:
        segundo += 1
    elif identificar_cuadrante(x, y) == 3:
        tercer += 1
    elif identificar_cuadrante(x, y) == 4:
        cuarto += 1

print("\nCantidad de puntos en cada cuadrante:")
print(f"\nPrimer Cuadrante: {primer}\nSegundo cuadrante: {segundo}\nTercer cuadrante: {tercer}\nCuarto cuadrante: {cuarto}")