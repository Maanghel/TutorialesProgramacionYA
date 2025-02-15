"""
Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, 
imprimir en pantalla la leyenda "Todos los números son menores a diez".
"""

def si_menores(entero1, entero2, entero3): # Funcion que evalua que los numeros sean menores a 10
    if entero1 < 10 and entero2 < 10 and entero3 < 10:
        print("Todos los numeros son menores a 10.")
    else:
        print("Al menos un numero no es menor a 10.")

#########################   Main    ################################

entero1 = int(input("Ingrese el primer entero: "))
entero2 = int(input("Ingrese el segundo entero: "))
entero3 = int(input("Ingrese el tercer entero: "))

si_menores(entero1, entero2, entero3)