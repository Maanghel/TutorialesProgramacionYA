"""
Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.
"""

# Funcion que retorna el promedio de tres enteros y los retorna
def promedio_enteros(v1,v2,v3):
    return (v1 + v2 + v3) / 3

# Funcion que carga tres enteros y los retorna
def cargar_enteros():
    entero1 = int(input("\nIngrese el primer entero: "))
    entero2 = int(input("Ingrese el segundo entero: "))
    entero3 = int(input("Ingrese el tercer entero: "))
    
    return [entero1, entero2, entero3]

#########################   Main    ################################

entero1, entero2, entero3 = cargar_enteros()

promedio = promedio_enteros(entero1, entero2, entero3)
print(f"\nEl promedio de los numeros ingresados es de {promedio}.")