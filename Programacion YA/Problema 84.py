"""
Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15.
"""

# Funcion que carga los productos y sus precios
def carga():
    productos = []
    for x in range(5):
        nom = input("\nIngrese el nombre del producto: ")
        prec = float(input("Ingrese el precio del producto: "))
        productos.append((nom, prec))
    
    return productos

# Funcion que imprime la lista
def imprimir(productos):
    print("\nLista de productos con su precio:")
    for prod, prec in productos:
        print(f"{prod}: {prec}")

# Funcion que imprime el nombre de los productos con un precio entre $10 y $15
def imprimir_precios_entre10y15(productos):
    print("\nProductos en los cuales su precio ronda entre los $10 y $15:")
    for prod, prec in productos:
        if prec >= 10 and prec <= 15:
            print(prod)

#########################   Main    ################################

productos = carga()
imprimir(productos)
imprimir_precios_entre10y15(productos)