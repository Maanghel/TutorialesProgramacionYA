"""
Problema 35: Reemplazar vocales por un símbolo específico
Crea una función llamada reemplazar_vocales que reciba una cadena y 
un símbolo (por ejemplo, * o #) como argumentos, y reemplace todas las vocales en la cadena por ese símbolo.
"""

def reemplazar_vocales(cadena, simbolo): # Funcion que reemplaza las vocales con algun simbolo
    vocales = "aeiouAEIOU"  # Se inicializa una variante con una string con las vocales minusculas y mayusculas
    
    for vocal in vocales: # Itera sobre la variante vocales
        cadena = cadena.replace(vocal, simbolo)  # Reemplaza cada vocal con el simbolo
    
    return cadena # Retorna la cadena modificada

#########################   Main    ################################

cadena = input("Ingrese una cadena: ")
simbolo = input("Ingrese el simbolo por el cual quiere que las vocales sean reemplazadas: ")

print(f"Cadena con las vocales reemplazadas:\n{reemplazar_vocales(cadena, simbolo)}")