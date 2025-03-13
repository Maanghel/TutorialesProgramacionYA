"""
Solicitar el ingreso del nombre de una persona y seleccionar de un control Listbox un país.
Al presionar un botón, mostrar en la barra de la ventana el nombre ingresado y el país seleccionado.
"""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        
        self.seleccion1 = tk.StringVar()
        self.label1 = tk.Label(self.ventana1, text = "Ingrese el nombre:")
        self.label1.grid(column = 0, row = 0)
        self.entry1 = tk.Entry(self.ventana1, width = 20, textvariable = self.seleccion1)
        self.entry1.grid(column = 1, row = 0)
        
        self.label2 = tk.Label(self.ventana1, text = "Seleccione pais:")
        self.label2.grid(column = 0, row = 1)
        self.listbox1 = tk.Listbox(self.ventana1)
        self.listbox1.grid(column = 1, row = 1)
        self.listbox1.insert(0, "Mexico")
        self.listbox1.insert(1, "Canada")
        self.listbox1.insert(2, "Estados Unidos")
        self.listbox1.insert(3, "Argentina")
        self.listbox1.insert(4, "Chile")
        self.listbox1.insert(5, "Brazil")
        self.listbox1.insert(6, "Peru")
        self.listbox1.insert(7, "Costa Rica")
        
        self.button1 = tk.Button(self.ventana1, text = "Mostrar", command = self.cambiar_titulo)
        self.button1.grid(column = 0, row = 2)
        
        self.ventana1.mainloop()
    
    def cambiar_titulo(self):
        # Funcion que cambia el titulo de la ventana
        if self.listbox1.curselection() != 0:
            self.ventana1.title(f"Nombre: {self.seleccion1.get()} - Pais: {self.listbox1.get(self.listbox1.curselection()[0])}")

#########################   Main    ################################

aplicacion = Aplicacion()