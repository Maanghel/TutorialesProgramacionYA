"""
Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de articulos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.
"""

# Funcion que carga los nombres y precios de los articulos
def carga():
    articulos = []
    precios = []
    for x in range(5):
        nom = input("\nIngrese el nombre del articulo: ")
        prec = float(input("Ingrese el precio del articulo: "))
        articulos.append(nom), precios.append(prec)
    
    return [articulos, precios]

# Funcion que imprime los articulos y sus precios
def imprimir_articulos_precios(articulos, precios):
    print("\nNombre del articulo y su precio:")
    for x in range(5):
        print(articulos[x], precios[x])

# Funcion que imprime el articulo con el mayor precio
def imprimir_mayor_precio(articulos, precios):
    posicion = 0
    mayor = precios[0]
    for x in range(1, len(precios)):
        if precios[x] > mayor:
            mayor = precios[x]
            posicion = x
    
    print(f"\nEl articulo con el mayor precio es {articulos[posicion]}.")

# Funcion que solicita un costo e imprime los articulos que son menores a el
def consulta_articulos_precio(articulos, precios):
    valor = float(input("\nIngrese un costo para mostrar los articulos menores al mismo: "))
    print("\nArticulos con un precio menor al indicado:")
    for x in range(5):
        if precios[x] <= valor:
            print(articulos[x])

#########################   Main    ################################

articulos, precios = carga()
imprimir_articulos_precios(articulos, precios)
imprimir_mayor_precio(articulos, precios)
consulta_articulos_precio(articulos, precios)