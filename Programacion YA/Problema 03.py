"""
Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio.
"""

def suma_promedio(entero1, entero2, entero3, entero4): # Funcion que retorna la suma y el promedio de los cuatro numeros
    suma = entero1 + entero2 + entero3 + entero4 # Suma los cuatro numeros
    promedio = suma / 4 # Saca el promedio de los numeros
    
    return [suma, promedio] # Retorna la suma y el promedio como lista

#########################   Main    ################################

entero1 = int(input("Ingrese el primer numero: "))
entero2 = int(input("Ingrese el segundo numero: "))
entero3 = int(input("Ingrese el tercer numero: "))
entero4 = int(input("Ingrese el cuarto numero: "))

print(f"La suma de los valores es: {suma_promedio(entero1, entero2, entero3, entero4)[0]}")
print(f"el promedio es de: {suma_promedio(entero1, entero2, entero3, entero4)[1]}")