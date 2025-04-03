"""
Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'.
"""

# Funcion que cuenta el total de a
def contar_a(mensaje):
    total_a = 0
    for vocal in mensaje.lower():
        if vocal == "a":
            total_a += 1
    
    return total_a

#########################   Main    ################################

mensaje = input("Ingrese un mensaje: ")

print(f"El total de 'a' y 'A' que contiene '{mensaje}' es de {contar_a(mensaje)}.")