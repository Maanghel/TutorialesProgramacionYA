"""
Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar la cantidad de vocales. 
Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal.
"""

def contar_vocales(cadena): # Funcion que cuenta las vocales
    total_vocales = 0
    
    for letra in cadena.lower(): # Se itera sobre la cadena en minusculas
        if letra in "aeiou": # Si la letra esta en "aeiou" devuelve True
            total_vocales += 1
    
    return total_vocales

#########################   Main    ################################

oracion = input("Ingrese una oracion para contar las vocales: ")

print(f"El total de vocales que tiene la oracion es de: {contar_vocales(oracion)}")