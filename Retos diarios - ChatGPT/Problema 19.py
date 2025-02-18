"""
Problema 19: Números de Fibonacci
Escribe una función que genere los primeros n números de la secuencia de Fibonacci. 
Recuerda que la secuencia de Fibonacci comienza con 0 y 1, y cada número posterior es la suma de los dos anteriores.
"""

def Fibonacci(entero): # Funcion que genera n numeros de la secuencia Fibonacci
    secuencia = [0, 1] # Se crea una lista con 0 y 1
    while len(secuencia) < entero: # Se realiza un while mientras la secuencia sea menor al entero
        siguiente = secuencia[-1] + secuencia[-2] # Se calcula el siguiente numero de la secuencia se obtiene sumando los dos ultimos numeros de la lista
        secuencia.append(siguiente)
    
    return secuencia[:entero] # Devuelve una porcion de la lista limitada a la cantidad de n numeros primeros

#########################   Main    ################################

entero = int(input("Ingrese un número: "))

print(f"La secuencia de Fibonacci es: {Fibonacci(entero)}")