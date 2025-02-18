"""
Problema 29: Encontrar los números primos dentro de un rango
Escribe una función que tome dos números enteros, inicio y fin, y retorne una 
lista de todos los números primos entre esos dos valores (inclusive). Recuerda que un número 
primo es aquel que solo es divisible por sí mismo y por 1.
"""

def verificar_primo(numero): # Funcion para verificar si un numero es primo o no
    if numero < 2: # Validacion para numeros menos a 2 ya que estos no son primos
        return False
    
    for x in range(2,numero):
        if numero % x == 0: # Valida que no haya un divisor exacto
            return False
    
    return True

def encontrar_primos(entero1, entero2): # Funcion que encuenra los numeros primos dentro de un rango
    lista_primos = [] # inicializa una lista vacia
    
    for x in range(entero1, entero2): # Itera sobre un rango dado
        if verificar_primo(x): # Se hace llamado a la funcion verificar primo, si es True lo agrega a la lista
            lista_primos.append(x)
    
    return lista_primos

#########################   Main    ################################

entero1 = int(input("Ingrese el numero inicial donde se empezara la verificacion: "))
entero2 = int(input("Ingrese el numero final donde se finalizara la verificacion: "))

print(f"Los numeros primos que se encuentran entre {entero1} y {entero2} son: {encontrar_primos(entero1, entero2)}")