"""
Problema 24: Contar Caracteres
Descripción: Crea una función que reciba una cadena de texto y devuelva un diccionario 
que contenga el conteo de cada carácter en la cadena. Asegúrate de que el conteo sea insensible a mayúsculas y minúsculas.
"""

def contar_caracteres(cadena): # Funcion que cuenta los caracteres
    conteo_caracteres = {} # Se inicializa un diccionario vacio
    
    for key in cadena.lower(): # Se itera sobre la cadena en minusculas
        if key in conteo_caracteres: # Si el caracter esta en el diccionario le agrega mas uno al value
            conteo_caracteres[key] += 1
        else: # En caso que no se agrega la letra y se inicializa su value en uno
            conteo_caracteres[key] = 1
    
    return conteo_caracteres 

#########################   Main    ################################

cadena = input("Ingrese una cadena de texto: ")

resultado = contar_caracteres(cadena)
print(resultado)