"""
Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. 
Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.
"""

def generar_lista_productos(): # Funcion que genera una dos listas que son paralelas
    lista_productos = []
    lista_precios = []
    
    for x in range(5):
        producto = input("Ingrese el nombre del producto: ")
        lista_productos.append(producto)
        precio = input("Ingrese el precio del producto: ")
        lista_precios.append(precio)
    
    return [lista_productos, lista_precios] # Retorn ambas listas

def mostar_mayores_primer(lista_productos, lista_precios): # Funcion que cuenta la cantidad de productos con un precio mayor al primero
    contador = 0
    
    for x in range(len(lista_precios)):
        if lista_precios[x] > lista_precios[0]:
            contador += 1
    
    return contador

#########################   Main    ################################

lista_productos, lista_precios = generar_lista_productos()

print(f"El numero de productos que tienen un precio mayor al primer producto ingresado son: {mostar_mayores_primer(lista_productos, lista_precios)}")