"""
Problema 39: Palabras con vocales
Escribe una función que reciba una cadena de texto y cuente 
cuántas palabras contienen una vocal. La función debe devolver 
el número total de palabras que contienen al menos una vocal (a, e, i, o, u).
"""

def palabras_vocal(cadena):
    vocales = set("aeiou")
    lista_palabras = cadena.lower().split()
    
    total = sum(1 for palabra in lista_palabras if any(letra in vocales for letra in palabra))
    
    return total

#########################   Main    ################################

cadena = input("Ingrese una cadena: ")
total_palabras_vocal = palabras_vocal(cadena)

if total_palabras_vocal == len(cadena.split()):
    print(f"{total_palabras_vocal} (Todas las palabras tienen al menos una vocal).")
elif total_palabras_vocal == 0:
    print(f"{total_palabras_vocal} palabras tienen al menos una vocal.")
else:
    print(f"La cadena tiene {total_palabras_vocal} palabras que contienen al menos una vocal.")