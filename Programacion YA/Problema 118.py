"""
Escribe un programa que haga lo siguiente:
cree y lea un archivo de texto llamado "texto.txt", el cual tiene que tener este contenido:
    Hola mundo, hola Python. Python es genial.
Cuente cuántas veces aparece cada palabra en el archivo.
Guarde el resultado en un nuevo archivo llamado "resultado.txt", mostrando cada palabra junto con su frecuencia.
"""

def crear_txt():
    # Funcion que crea un archivo de texto y escribe una linea especifica en el
    with open("texto.txt", "w", encoding= "utf-8") as archivo:
        archivo.write("Hola mundo, hola Python. Python es genial.")

def contar_palabras():
    # Funcion que cuenta las palabras en un archivo y almacena los resultados en un nuevo archivo
    with open("texto.txt", "r", encoding= "utf-8") as archivo:
        contenido = archivo.read().lower()
    
    for char in ",.":
        contenido = contenido.replace(char, "")
    
    palabras = contenido.split()
    
    conteo_palabras = {}
    for palabra in palabras:
        if palabra in conteo_palabras:
            conteo_palabras[palabra] += 1
        else:
            conteo_palabras[palabra] = 1
    
    with open("resultado.txt", "w", encoding= "utf-8") as archivo:
        for palabra, cantidad in conteo_palabras.items():
            archivo.write(f"{palabra}: {cantidad}\n")

#########################   Main    ################################

crear_txt()
contar_palabras()