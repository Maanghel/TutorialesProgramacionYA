"""
Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. 
Llamarla desde el bloque principal del programa 3 veces con string distintos.
"""

# Funcion que cuenta las vocales de un mensaje y las devuelve
def contar_vocales(mensaje):
    vocales = 0
    for vocal in mensaje.lower():
        if vocal in "aeiou":
            vocales += 1
    
    print(f"La cantidad de vocales que contiene '{mensaje}' es de {vocales}.")

#########################   Main    ################################

contar_vocales("Hola Mundo.")
contar_vocales("Aprendiendo Python.")
contar_vocales("Adios Mundo.")