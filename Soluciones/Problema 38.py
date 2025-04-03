"""
Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. 
Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, 
en caso contrario mostrar un mensaje de error.
"""

def validar_tamaño(clave): # Funcion que verifica la longitud de una clave
    if len(clave) <= 20 and len(clave) >= 10:
        print("La clave es correcta.")
    else:
        print("Clave incorrecta. Ingrese una clave con los caracteres especificados.")

#########################   Main    ################################

cadena = input("Ingrese una clave (10 a 20 caracteres): ")

validar_tamaño(cadena)