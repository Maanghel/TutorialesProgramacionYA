"""
Problema 46: Encontrar la subcadena más larga sin caracteres repetidos
Dada una cadena de texto, escribe una función que encuentre la subcadena más 
larga que no contenga caracteres repetidos. La subcadena puede estar formada por 
letras, números o cualquier símbolo, siempre y cuando no haya duplicados dentro de esa subcadena.
"""

def subcadena_larga_sin_repetidos(cadena): # Funcion que encuentra la subcadena mas larga
    inicio = 0  # Puntero inicial de la subcadena
    max_longitud = 0  # Longitud máxima encontrada
    caracteres = set()  # Conjunto para almacenar caracteres únicos
    
    for fin in range(len(cadena)):  # Puntero final que recorre la cadena
        while cadena[fin] in caracteres:
            caracteres.remove(cadena[inicio]) # Eliminar el carácter al que apunta 'inicio' y mover el puntero
            inicio += 1
        
        caracteres.add(cadena[fin]) # Añadir el nuevo carácter al conjunto
        
        max_longitud = max(max_longitud, fin - inicio + 1) # Actualizar la longitud máxima
    
    return max_longitud

#########################   Main    ################################

cadena = input("Ingrese una cadena de caracteres: ")

print(f"La longitud de la subcadena más larga sin caracteres repetidos es: {subcadena_larga_sin_repetidos(cadena)}")