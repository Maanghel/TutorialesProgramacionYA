"""
Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el número 
de documento del alumno. Como valor almacenar una lista con componentes de tipo tupla donde 
almacenamos nombre de materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.
"""

# Funcion que carga un diccionario
def carga():
    diccionario = {}
    
    for x in range(3):
        numero = int(input("\nIngrese el DNI del alumno: "))
        lista = []
        continuar = "s"
        while continuar == "s":
            materia = input("\nIngrese la materia: ")
            calif = float(input("Ingrese la calificacion: "))
            lista.append((materia, calif))
            continuar = input("Desea ingresar la calificacion de otra materia: [s/n] ")
        diccionario[numero] = lista
    
    return diccionario

# Funcion que imprime el diccionario
def imprimir(diccionario):
    print("\nCalificaciones del alumno:")
    for numero in diccionario:
        print(f"\nDNI del alumno: {numero}")
        print("Materias y sus notas:")
        for materia, nota in diccionario[numero]:
            print(f"{materia}: {nota}")

# Funcion que consulta las materias y las calificaciones de un alumno
def consulta_materias(diccionario):
    numero = int(input("\nIngrese el DNI del alumno: "))
    if numero in diccionario:
        print(f"Materias y sus calificaciones:")
        for materia, nota in diccionario[numero]:
            print(f"{materia}: {nota}")
            
#########################   Main    ################################

diccionario = carga()
imprimir(diccionario)
consulta_materias(diccionario)