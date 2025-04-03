"""
Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, 
imprimir en pantalla la leyenda "Alguno de los números es menor a diez".
"""

def si_menores(entero1, entero2, entero3): # Funcion que evalua que al menos un numero sea menor a 10
    if entero1 < 10 or entero2 < 10 or entero3 < 10:
        print("Alguno de los numeros es menor a 10.")
    else:
        print("Todos los numeros son mayores a 10.")

#########################   Main    ################################

entero1 = int(input("Ingrese el primer entero: "))
entero2 = int(input("Ingrese el segundo entero: "))
entero3 = int(input("Ingrese el tercer entero: "))

si_menores(entero1, entero2, entero3)