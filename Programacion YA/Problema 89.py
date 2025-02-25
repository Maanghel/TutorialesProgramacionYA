"""
Cargar una cadena por teclado luego:
1) Imprimir los dos primeros caracteres.
2) Imprimir los dos últimos
3) Imprimir todos menos el primero y el último caracter.
"""

# Funcion que carga una cadena de caracteres
def carga():
    cadena = input("Ingrese una cadena de caracteres: ")
    return cadena

# Funcion que imprime los dos primeros, los dos ultimos y todos excepto el primero y ultimo caracter de una cadena
def imprimir(cadena):
    print(f"\nPrimeros dos caracteres: {cadena[:2]}")
    print(f"\nUltimos dos caracteres: {cadena[-2:]}")
    print(f"\nTodos los caracteres excepto el primero y ultimo: {cadena[1:-1]}")

#########################   Main    ################################

cadena = carga()
imprimir(cadena)