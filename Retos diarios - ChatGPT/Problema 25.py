"""
Problema 25: Encontrar Palabras Más Largas
Descripción: Escribe una función que reciba una cadena de texto y 
devuelva una lista de las palabras más largas en esa cadena. Si hay varias 
palabras con la misma longitud máxima, devuélvelas todas.
"""

def encontrar_palabras_largas(cadena): # Funcion que encuentra la o las palabras mas largas
    lista_palabras = cadena.split() # Crea una lista de la cadena
    longitud_maxima = 0 # inicializa una variable en 0 de la longitud maxima encontrada
    palabras_mas_largas = [] # Se inicializa una lista vacia para la o las palabras mas largas
    
    for palabra in lista_palabras: # Itera sobre la lista de palabras
        if len(palabra) > longitud_maxima: # Si la palabra es mayor que la lonitud maxima encontrada
            longitud_maxima = len(palabra) # Se actualiza la longitud maxima
            palabras_mas_largas = [palabra] # Actualiza la lista
        elif len(palabra) == longitud_maxima: # Si la palabra es igual a la longitud maxima
            palabras_mas_largas.append(palabra) # Agrega la palabra a la lista
    
    return palabras_mas_largas

#########################   Main    ################################

cadena = input("Ingrese una cadena de palabras: ")

print(f"Las palabras más largas son: {', '.join(encontrar_palabras_largas(cadena))}") # Imprimie las dos listas y las concatena separadas con una coma con la funcion join