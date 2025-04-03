"""
Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe 
cuántos tienen notas mayores o iguales a 7 y cuántos menores.
"""

def notas_mayores7(): # Funcion que contabiliza las notas mayores a 7 y las menores a este tambien
    contador_mayores = 0
    contador_menores = 0
    for x in range(10):
        nota = int(input("Ingrese la nota del alumno (rando de 0-10): "))
        if nota >= 7:
            contador_mayores += 1
        else:
            contador_menores += 1
    
    return [contador_mayores, contador_menores]

#########################   Main    ################################

mayores, menores = notas_mayores7()

print(f"El total de alumnos con notas mayores o iguales a 7 son: {mayores}")
print(f"El total de alumnos con notas menores a 7 son: {menores}")