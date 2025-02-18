"""
Problema 26: Remover duplicados de una lista
Escribe una función que tome una lista de números enteros como argumento y 
retorne una nueva lista con todos los números duplicados eliminados. Debes mantener el orden original de los números en la lista.
"""

def retornar_duplicados(cadena): # Funcion que remueve los duplicados de una lista de enteros
    lista_enteros = list(map(int, cadena.split())) # Convierte la cadena en una lista de enteros
    lista_sin_duplicados = [] # Inicializa una lista para la nueva lista
    
    for numero in lista_enteros: # Itera sobre la lista de enteros
        if numero not in lista_sin_duplicados: # Si el entero no esta en la lista sin duplicados 
            lista_sin_duplicados.append(numero) # Agrega al entero a la lista
    
    return lista_sin_duplicados # Retorna la lista sin duplicados

#########################   Main    ################################

cadena = input("Ingrese una lista de números enteros (separados por espacios): ")

print(f"Nueva lista con los elementos duplicados eliminados: {retornar_duplicados(cadena)}")