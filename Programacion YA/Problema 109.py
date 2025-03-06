"""
Disponer varios objetos de la clase Checkbutton con nombres de navegadores web.
En el título de la ventana mostrar todos los nombres de navegadores seleccionados.
"""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        
        self.seleccion1 = tk.IntVar()
        self.check1 = tk.Checkbutton(self.ventana1, text = "Google Chrome", variable = self.seleccion1)
        self.check1.grid(column = 0, row = 0)
        
        self.seleccion2 = tk.IntVar()
        self.check2 = tk.Checkbutton(self.ventana1, text = "Internet Explorer", variable = self.seleccion2)
        self.check2.grid(column = 0, row = 1)
        
        self.seleccion3 = tk.IntVar()
        self.check3 = tk.Checkbutton(self.ventana1, text = "Mozilla Firefox", variable = self.seleccion3)
        self.check3.grid(column = 0, row = 2)
        
        self.button1 = tk.Button(self.ventana1, text = "Mostrar", command = self.modificar_titulo)
        self.button1.grid(column = 0, row = 3)
        
        self.ventana1.mainloop()
        
    def modificar_titulo(self):
        cadena = ""
        if self.seleccion1.get() == 1:
            cadena += "Google Chrome - "
        if self.seleccion2.get() == 1:
            cadena += "Internet Explorer - "
        if self.seleccion3.get() == 1:
            cadena += "Mozilla Firefox - "
        
        self.ventana1.title(cadena)

#########################   Main    ################################

aplicacion = Aplicacion()