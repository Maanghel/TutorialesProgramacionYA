"""
Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro. 
Definir un segundo parámetro llamado termino que por defecto almacene el valor 10. Se deben mostrar
tantos términos de la tabla de multiplicar como lo indica el segundo parámetro.
Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.
"""

# Funcion que imprime los multiplos de un valor
def tabla_multiplicar(valor, termino = 10):
    for x in range(1, termino + 1):
        print(valor * x, ",", sep = "", end = "")

#########################   Main    ################################

print("\nTabla del 3:")
tabla_multiplicar(valor = 3)

print("\nTabla del 5 con 5 termino:")
tabla_multiplicar(valor = 5, termino = 5)