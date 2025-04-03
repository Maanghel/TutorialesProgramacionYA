"""
Confeccionar una función que reciba una serie de edades y me retorne 
la cantidad que son mayores o iguales a 18 (como mínimo se envía un entero a la función)
"""

# Funcion que retorna la cantidad de edades mayores de 18
def mayor_edad(edad1, *edades):
    total = 0
    
    for edad in edades:
        if edad >= 18:
            total += 1
    
    return total

#########################   Main    ################################

print(f"La cantidad de personas mayores de 18 años son: {mayor_edad(1, 19, 20, 15, 23, 14)}")