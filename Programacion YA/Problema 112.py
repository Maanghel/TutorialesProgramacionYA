"""
Mediante dos controles de tipo Entry permitir el ingreso de dos números. 
Crear un menú que contenga una opción que cambie el tamaño de la ventana 
con los valores ingresados por teclado. Finalmente disponer otra opción que finalice el programa
"""

import tkinter as tk
from tkinter import ttk
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Prueba")
        
        menu1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu = menu1)
        opciones1 = tk.Menu(menu1, tearoff = 0)
        opciones1.add_command(label = "Resolucion ingresada", command = self.cambiar_tamaño)
        opciones1.add_separator()
        opciones1.add_command(label = "Salir", command = self.salir)
        menu1.add_cascade(label = "Modificar ventana", menu = opciones1)
        
        self.label1 = ttk.Label(self.ventana1, text = "Introducir el ancho de la ventana:")
        self.label1.grid(column = 0, row = 0)   
        self.seleccion1 = tk.StringVar()
        self.entry1 = ttk.Entry(self.ventana1, width = 5, textvariable = self.seleccion1)
        self.entry1.grid(column = 1, row = 0)
        
        self.label2 = ttk.Label(self.ventana1, text = "Introducir el largo de la ventana:")
        self.label2.grid(column = 0, row = 1)
        self.seleccion2 = tk.StringVar()
        self.entry2 = ttk.Entry(self.ventana1, width = 5, textvariable = self.seleccion2)
        self.entry2.grid(column = 1, row = 1)
        
        self.ventana1.mainloop()
    
    def cambiar_tamaño(self):
        self.ventana1.geometry(f"{self.seleccion1.get()}x{self.seleccion2.get()}")
    
    def salir(self):
        sys.exit()

#########################   Main    ################################

aplicacion = Aplicacion()