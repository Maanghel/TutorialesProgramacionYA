"""
Solicitar el ingreso del nombre de una persona y seleccionar de un control Combobox un país.
Al presionar un botón mostrar en la barra de la ventana el nombre ingresado y el país seleccionado.
"""

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        
        self.seleccion1 = tk.StringVar()
        self.label1 = ttk.Label(self.ventana1, text = "Ingrese el nombre:")
        self.label1.grid(column = 0, row = 0)
        self.entry1 = ttk.Entry(self.ventana1, width = 20, textvariable = self.seleccion1)
        self.entry1.grid(column = 1, row = 0)
        
        self.label2 = ttk.Label(self.ventana1, text = "Seleccione pais:")
        self.label2.grid(column = 0, row = 1)
        paises = ("Mexico", "Canada", "Colombia", "Argentina", "Chile", "Estados Unidos")
        self.seleccion2 = tk.StringVar()
        self.combobox1 = ttk.Combobox(self.ventana1,
                                    width = 10,
                                    textvariable = self.seleccion2,
                                    values = paises,
                                    state = "readonly")
        self.combobox1.current(0)
        self.combobox1.grid(column = 1, row = 1)
        
        self.button1 = ttk.Button(self.ventana1, text = "Mostrar", command = self.cambiar_titulo)
        self.button1.grid(column = 0, row = 2)
        
        self.ventana1.mainloop()
    
    def cambiar_titulo(self):
        self.ventana1.title(f"Nombre: {self.seleccion1.get()} - Pais: {self.seleccion2.get()}")

#########################   Main    ################################

aplicacion = Aplicacion()