"""
Problema 36: Contar Palabras Específicas en una Cadena
Escribe una función llamada contar_palabra_especifica(cadena, palabra) 
que cuente cuántas veces aparece una palabra específica en una cadena dada. 
La función debe ignorar mayúsculas y minúsculas.
"""

import re # Importa la funcion para expresiones regulares

def contar_palabra_especifica(cadena, palabra): # Contar las palabras especificas de una cadena
    cadena = re.sub(r'[^\w\s]', '', cadena.lower()) # Elimina todo lo que no sea palabra, numero o espacio
    lista_palabras = cadena.split() # Crea una lista con las palabras en minusculas
    
    return lista_palabras.count(palabra)  # Usa el método count para contar directamente

#########################   Main    ################################

cadena = input("Ingrese una cadena de palabras: ")
palabra = input("Ingrese la palabra especifica que desea contar: ")

print(f"La cantidad de veces que aparece {palabra} es de: {contar_palabra_especifica(cadena,palabra)}")