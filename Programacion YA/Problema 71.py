"""
Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. 
Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))
"""

# Funcion que devuelve la palabra con mas caracteres
def mascaracteres(palabras):
    posicion = 0
    for x in range(len(palabras)):
        if len(palabras[x]) > len(palabras[posicion]):
            posicion = x
    
    return palabras[posicion]

#########################   Main    ################################

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]

print("Palabra con mas caracteres:",mascaracteres(palabras))