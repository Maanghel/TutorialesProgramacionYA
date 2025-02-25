"""
Cargar una cadena de caracteres por teclado. Mostrar la cadena del final al principio utilizando subíndices negativos.
"""

# Funcion que carga una cadena de caracteres
def carga():
    cadena = input("Ingrese una cadena de caracteres: ")
    return cadena

# Funcion que imprime de derecha a izquiera una cadena
def imprimir(cadena):
    indice = -1
    for x in range(len(cadena)):
        print(cadena[indice])
        indice -= 1

#########################   Main    ################################

cadena = carga()
imprimir(cadena)