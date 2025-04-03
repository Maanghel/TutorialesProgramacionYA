"""
Definir una función que cargue una lista con palabras y la retorne.
Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres.
"""

# Funcion que carga una lista de palabras
def carga():
    palabras = []
    total_palabras = int(input("\nIngrese el total de palabras a almacenar: "))
    for x in range(total_palabras):
        pala = input("Ingrese la palabra: ")
        palabras.append(pala)
    
    return palabras

# Funcion que muestra las palabras con mas de cinco caracteres
def mostrar_mas5_caracteres(palabras):
    print("\nPalabras que tienen mas de 5 caracteres:")
    for pala in palabras:
        if len(pala) > 5:
            print(pala)

#########################   Main    ################################

palabras = carga()
mostrar_mas5_caracteres(palabras)