"""
Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. 
La segunda que solicite la carga de dos valores y muestre el producto de los mismos. LLamar desde el bloque del programa principal a ambas funciones.
"""

# Funcion que imprime el cuadrado del entero ingresado
def cargar_entero_cuadrado():
    entero = int(input("\nIngrese un entero: "))
    
    print(f"El cuadrado de {entero} es", entero ** 2)

# Funcion que imprime el producto de los enteros ingresados
def cargar_enteros_producto():
    entero1 = int(input("\nIngrese el primer entero:"))
    entero2 = int(input("Ingrese el segundo entero:"))
    
    print(f"El producto de {entero1} por {entero2} es", entero1 * entero2)

#########################   Main    ################################

cargar_entero_cuadrado()
cargar_enteros_producto()