"""
Problema 31: Segundo mas pequeño
Escribe una función que reciba una lista de enteros y devuelva el segundo número más pequeño en la lista.
"""

def segundo_pequeño(cadena): # Funcion que retorna el segundo numero mas pequeño
    lista_enteros = sorted(set(map(int, cadena.split()))) # convierte a un conjunto la cadena y la ordena ascendentemente
    
    if len(lista_enteros) < 2: # Verifica si la lista tiene menos de dos enteros
        return "La lista no tiene suficientes números únicos."
    
    return lista_enteros[1] # Retorna el segundo numero de la lista

#########################   Main    ################################

cadena = input("Ingrese una lista de enteros (separados por espacios):")

print(f"El segundo número mas pequeño es {segundo_pequeño(cadena)}.")