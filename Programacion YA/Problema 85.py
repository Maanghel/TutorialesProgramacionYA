"""
Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento.
"""

# Funcion que carga un diccionario
def carga():
    diccionario = {}
    for x in range(4):
        numero = int(input("\nIngrese el numero del documento: "))
        nombre = input("Ingrese el nombre de la persona: ")
        diccionario[numero] = nombre
    
    return diccionario

# Funcion que imprime un diccionario
def imprimir_diccionario(diccionario):
    print("\nNumero de documento y nombre de la persona:")
    for numero in diccionario:
        print(f"{numero}: {diccionario[numero]}")

# Funcion que consulta un numero de documento en el diccionario
def consultar_nombre(diccionario):
    numero = int(input("\nIngrese el numero de documento: "))
    if numero in diccionario:
        print(f"\nEl numero {numero} de documento corresponde a {diccionario[numero]}.")
    else:
        print("\nNo existe una persona con el numero de documento ingresado.")

#########################   Main    ################################

diccionario = carga()
imprimir_diccionario(diccionario)
consultar_nombre(diccionario)