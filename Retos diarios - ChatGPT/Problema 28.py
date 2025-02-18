"""
Problema 28: Encontrar la intersección de dos listas de enteros
Escribe un programa que acepte dos listas de enteros y devuelva una nueva lista 
que contenga los elementos que están en ambas listas (intersección de las dos listas), sin duplicados.
"""

def retornar_interseccion(cadena1, cadena2): # Funcion que retorna la interseccion de dos listas
    lista_enteros1 = set(map(int, cadena1.split())) # Convierte en una lista de enteros la cadena
    lista_enteros2 = set(map(int, cadena2.split())) # Convierte en una lista de enteros la cadena
    
    lista_interseccion = list(lista_enteros1 & lista_enteros2) # Usamos el operador de intersección de conjuntos (&)
    
    return lista_interseccion # Retorna la lista de interseccion

#########################   Main    ################################

cadena1 = input("Ingrese la primer lista de números enteros (separados por espacios): ")
cadena2 = input("Ingrese la segunda lista de números enteros (separados por espacios): ")

print(f"La intersección de ambas listas es: {retornar_interseccion(cadena1, cadena2)}")