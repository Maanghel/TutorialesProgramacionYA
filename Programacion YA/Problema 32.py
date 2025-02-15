"""
Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
    a) Obtener el promedio de las edades de cada turno (tres promedios)
    b) Imprimir dichos promedios (promedio de cada turno)
    c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.
"""

def promedio_edad(mañana, tarde, noche): # Funcion que retorna los promedios de edad de cada turno
    promedio_mañana = sum(mañana) / len(mañana)
    promedio_tarde = sum(tarde) / len(tarde)
    promedio_noche = sum(noche) / len(noche)
    
    return [promedio_mañana, promedio_tarde, promedio_noche] # Los retorna como datos tipo lista

def promedio_mayor(promedio_mañana, promedio_tarde, promedio_noche): # Funcion que busca el promedio mayor
    if promedio_mañana > promedio_tarde and promedio_mañana > promedio_noche:
        return print("\nLa mañana tiene el promedio de edad mas alto.")
    elif promedio_tarde > promedio_mañana and promedio_tarde > promedio_noche:
        return print("\nLa tarde tiene el promedio de edad mas alto.")
    else:
        return print("\nLa noche tiene el promedio de edad mas alto.")

#########################   Main    ################################

edades_mañana = []
edades_tarde = []
edades_noche = []

for x in range(5):
    edad = int(input("Ingrese la edad del alumno de la mañana: "))
    edades_mañana.append(edad)

for x in range(6):
    edad = int(input("Ingrese la edad del alumno de la tarde: "))
    edades_tarde.append(edad)

for x in range(11):
    edad = int(input("Ingrese la edad del alumno de la noche: "))
    edades_noche.append(edad)

promedio_mañana, promedio_tarde, promedio_noche = promedio_edad(edades_mañana, edades_tarde, edades_noche)

print(f"\nPromedio de edades:\nMañana: {promedio_mañana}\nTarde: {promedio_tarde}\nNoche: {promedio_noche}")

promedio_mayor(promedio_mañana, promedio_tarde, promedio_noche)