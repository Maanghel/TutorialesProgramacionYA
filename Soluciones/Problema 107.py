"""
Ingresar el nombre de usuario y clave en controles de tipo Entry. 
Si se ingresa las cadena (usuario: juan, clave="abc123") luego mostrar en el 
título de la ventana el mensaje "Correcto" en caso contrario mostrar el mensaje "Incorrecto".
Para mostrar '*' cuando se ingresa la clave debemos pasar en el parámetro 'show' el caracter a mostrar:
        self.entry2=tk.Entry(self.ventana1, width=30, textvariable=self.dato2, show="*")
"""

import tkinter as tk

class Aplicacion:
    def __init__(self, usuario, clave):
        self.usuario = usuario
        self.clave = clave
        
        self.ventana1 = tk.Tk()
        self.ventana1.title("Login")
        
        self.label1 = tk.Label(self.ventana1, text = "Usuario")
        self.label1.grid(column = 0, row = 0)
        self.datos1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width = 20, textvariable = self.datos1)
        self.entry1.grid(column = 1, row = 0)
        
        self.label2 = tk.Label(self.ventana1, text = "Clave")
        self.label2.grid(column = 0, row = 1)
        self.datos2 = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana1, width = 20, textvariable = self.datos2, show = "*")
        self.entry2.grid(column = 1, row = 1)
        
        self.button1 = tk.Button(self.ventana1, text = "Login", command = self.login)
        self.button1.grid(column = 1, row = 2)
        
        self.ventana1.mainloop()
    
    def login(self):
        # Funcion que verifica si el usuario y contraseña son correctos
        if self.datos1.get() == self.usuario and self.datos2.get() == self.clave:
            self.ventana1.title("Correcto")
        else:
            self.ventana1.title("Incorrecto")

#########################   Main    ################################

aplicacion = Aplicacion("Juan", "abc123")