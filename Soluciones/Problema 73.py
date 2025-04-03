"""
En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.
"""

# Funcion que genera una lista de enteros
def cargar_sueldos():
    lista = []
    for x in range(10):
        val = float(input("Ingrese el sueldo del empleado: "))
        lista.append(val)
    
    return lista

# Funcion que imprime una lista de sueldos
def imprimir_sueldos(lista):
    print("\nLista de sueldos:")
    for x in range(10):
        print(lista[x])

# Funcion que imprime el total de sueldos que superan los $4000
def total_mayor4000(lista):
    total = 0
    for valor in lista:
        if valor > 4000:
            total += 1
    
    print(f"\nTotal de empleados con un sueldo superior a $4000: {total}")

# Funcion que devuelve el promedio de la lista
def promedio_sueldos(lista):
    return sum(lista) / 10

# Funcion que imprime el promedio y los sueldos inferiores a este
def imprimir_menores_promedio(lista, promedio):
    print(f"\nSueldo promedio de la empresa: {promedio}")
    print(f"\nSueldos que estan debajo de ese promedio:")
    for valor in lista:
        if valor < promedio:
            print(valor)

#########################   Main    ################################

lista_sueldos = cargar_sueldos()
imprimir_sueldos(lista_sueldos)
total_mayor4000(lista_sueldos)
promedio = promedio_sueldos(lista_sueldos)
imprimir_menores_promedio(lista_sueldos, promedio)