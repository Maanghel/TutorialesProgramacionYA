"""
Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. 
Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es ""
"""

def contar_espacios(cadena): # Funcion que cuenta los espacios en blanco
    total_espacios = 0
    
    for letra in cadena:
        if letra == " ":
            total_espacios += 1
    
    return total_espacios

#########################   Main    ################################

oracion = input("Igrese una oracion para contar sus espacios: ")

print(f"El total de espacios que tiene la oracion es de: {contar_espacios(oracion)}")