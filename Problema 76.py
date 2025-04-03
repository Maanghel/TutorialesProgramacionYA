"""
Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos debe retornar la suma de dichos valores.
Debe tener tres parámetros por defecto.
"""

# Funcion que hace uso de parametros con valor por defecto
def suma(entero1, entero2, entero3 = 0, entero4 = 0, entero5 = 0):
    return entero1 + entero2 + entero3 + entero4 + entero5

#########################   Main    ################################

print("\nLa suma de 3 + 4")
print(suma(3, 4))

print("\nLa suma de 3 + 4 + 7")
print(suma(3, 4, 7))

print("\nLa suma de 3 + 4 + 7 + 10")
print(suma(3, 4, 7, 10))