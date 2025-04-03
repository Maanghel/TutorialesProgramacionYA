"""
Se ingresan tres valores por teclado, si todos son iguales se imprime la 
suma del primero con el segundo y a este resultado se lo multiplica por el tercero.
"""

def si_iguales(entero1, entero2, entero3): # Funcion que si todos los numeros son iguales, suma los dos primeros y los multiplica por el tercero
    if entero1 == entero2 and entero1 == entero3:
        return (entero1 + entero2) * entero3

#########################   Main    ################################

entero1 = int(input("Ingrese el primer entero: "))
entero2 = int(input("Ingrese el segundo entero: "))
entero3 = int(input("Ingrese el tercer entero: "))

if si_iguales(entero1, entero2, entero3) != None:
    print(f"El resultado de sumar los dos primeros y multiplicarlo por el tercero es: {si_iguales(entero1, entero2, entero3)}")
else:
    print("Al menos un numero era diferente.")