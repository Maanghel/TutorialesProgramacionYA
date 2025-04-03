"""
Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
c - Calcular la temperatura media trimestral de cada país.
c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
b - Imprimir el nombre del pais con la temperatura media trimestral mayor.
"""

# Funcion que carga los paises y las temperaturas de los ultimos 3 meses
def cargar_temperaturas():
    paises = []
    temperaturas = []
    
    for x in range(4): # Ciclo For que ingresa los nombres y temperaturas
        nom = input("\nIngrese el nombre del pais: ")
        temp = []
        for y in range(3):
            temp.append(int(input(f"Ingrese la temperatura media del mes {y+1}: ")))

        paises.append(nom), temperaturas.append(temp)
    
    return [paises, temperaturas]

# Funcion que imprime las temperaturas y los paises
def imprimir_temperaturas(paises, temperaturas):
    for x in range(4):
        print(f"\nNombre del pais: {paises[x]}")
        print(f"Temperaturas medias mensuales: {temperaturas[x]}")

# Funcion que calcula la temperatura media trimestral de cada pais
def calcular_temperatura_media_trimestral(paises, temperaturas):
    temp_media_trimestral = []
    
    for x in range(4):
        temp_media_trimestral.append(sum(temperaturas[x])/3) # Calcula la media y la asigna a la lista temp_media_trimestral
    
    return temp_media_trimestral

# Funcion que imprime los paises y la temperatura media trimestral
def imrpimir_paises_media_trimestral(paises, temp_media_trimestral):
    for x in range(4):
        print(f"\nNombre del pais: {paises[x]}")
        print(f"Temperatura media trimestral: {temp_media_trimestral[x]}")

# Funcion que calcula el pais con la mayor temperatura media trimestral
def pais_temperatura_mayor(paises, temp_media_trimestral):
    mayor = 0
    pais = ""
    
    for x in range(4):
        if temp_media_trimestral[x] > mayor:
            mayor = temp_media_trimestral[x]
            pais = paises[x]
    
    return pais


#########################   Main    ################################

paises, temperaturas = cargar_temperaturas()
imprimir_temperaturas(paises, temperaturas)
temp_media_trimestral = calcular_temperatura_media_trimestral(paises, temperaturas)
imrpimir_paises_media_trimestral(paises, temp_media_trimestral)

print(f"\nEl pais con la temperatura media trimestral mayor es: {pais_temperatura_mayor(paises, temp_media_trimestral)}")