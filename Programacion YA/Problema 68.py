"""
Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
"""

# Funcion que retorna el area de un rectangulo
def retornar_superficie(lado1, lado2):
    return lado1 * lado2

# Funcion que carga el largo y lo alto de un rectangulo
def cargar():
    largo = float(input("Ingrese el largo del rectangulo: "))
    alto = float(input("Ingrese lo alto del rectangulo: "))
    
    return [largo, alto]

#########################   Main    ################################

largo, alto = cargar()

print(f"\nEl area del rectangulo es de {retornar_superficie(largo, alto)}.")