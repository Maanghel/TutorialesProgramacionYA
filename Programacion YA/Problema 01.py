"""
Realizar la carga del lado de un cuadrado, mostrar por pantalla el perímetro del mismo 
(El perímetro de un cuadrado se calcula multiplicando el valor del lado por cuatro)
"""

def perimetro_cuadrado(lado): # funcion que retorna el perimetro de un cuadrado
    return lado + lado + lado + lado # Retorna la suma de cuatro lados

#########################   Main    ################################

lado = int(input("Ingrese el lado del cuadrado: "))

print(f"El perimetro del cuadrado es: {perimetro_cuadrado(lado)}")