"""
Problema 40: Numeros Repetidos
Escribe un programa que reciba una cadena de texto que contenga varios números 
enteros separados por espacios. El programa debe devolver el número que más se repite, 
y en caso de que haya más de uno con la misma frecuencia, debe devolver el mayor de ellos.
"""

import collections # Importa el modulo collections para alternativas a las estructuras de datos

def contar_repetidos(cadena): # Funcion que retorna el o los numeros con mayor frecuencia en la cadena
    lista_enteros = list(map(int, cadena.split())) # Convierte la cadena en una lista que es convertida a entero
    
    numeros_repeticion = collections.Counter(lista_enteros) # Crea un diccionario con las keys como los numeros y las values como la frecuencia que aparecen
    
    max_frecuencia = max(numeros_repeticion.values()) # Se busca la mayor frecuencia
    
    numeros_mas_frecuentes = [num for num, freq in numeros_repeticion.items() if freq == max_frecuencia] # Se utiliza la compresion de lista para generar una lista con los numeros que tienen la misma frecuencia maxima
    
    return max(numeros_mas_frecuentes), max_frecuencia # Retorna el maximo de la lista de numeros mas frecuentes y la frecuencia maxima

#########################   Main    ################################

cadena = input("Ingrese una lista de enteros (separados por espacios): ")

numero, frecuencia = contar_repetidos(cadena) # Se asignan los resultados a las variables
print(f"El número que más se repite es {numero} y se repite {frecuencia} veces.")