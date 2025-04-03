"""
Crea una aplicación en Tkinter que permita al usuario:
    Seleccionar un archivo de texto (.txt) desde su computadora.
    Mostrar en pantalla cuántas líneas, palabras y caracteres tiene el archivo.
"""

import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import filedialog as fd
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.agregar_menu()
        self.scrolledtext1 = st.ScrolledText(self.ventana1, width= 80, height= 20)
        self.scrolledtext1.grid(column= 0, row= 0, padx= 10, pady= 10)
        self.scrolledtext1.config(state= tk.DISABLED)
        
        self.label_lineas = tk.Label(self.ventana1, text= "Lineas: 0")
        self.label_lineas.grid(column= 0, row= 1, padx= 10, pady= 5, sticky= "w")
        
        self.label_palabras = tk.Label(self.ventana1, text= "Palabras: 0")
        self.label_palabras.grid(column= 0, row= 2, padx= 10, pady= 5, sticky= "w")
        
        self.label_caracteres = tk.Label(self.ventana1, text="Caracteres: 0")
        self.label_caracteres.grid(column= 0, row= 3, padx= 10, pady= 5, sticky= "w")
        
        self.ventana1.mainloop()
    
    def agregar_menu(self):
        # Funcion que agrega un menu en la ventana
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu= menubar1)
        opciones1 = tk.Menu(menubar1, tearoff= 0)
        opciones1.add_command(label= "Seleccionar archivo", command= self.seleccionar)
        opciones1.add_separator()
        opciones1.add_command(label= "Salir", command= self.salir)
        menubar1.add_cascade(label= "Archivo", menu= opciones1)
    
    def salir(self):
        # Funcion que cierra la ejecucion del programa
        sys.exit()
    
    def seleccionar(self):
        # Funcion que recupera un archivo y los despliega en el scrolled text
        nombre_archivo = fd.askopenfilename(initialdir= "/", title= "Seleccione archivo", filetypes= (("txt files", "*.txt"), ("todos los archivos", "*.*")))
        if nombre_archivo:
            with open(nombre_archivo, "r", encoding= "utf-8") as archivo:
                contenido = archivo.read()
            
            num_lineas = len(contenido.splitlines())
            num_palabras = len(contenido.split())
            num_caracteres = len(contenido)
            
            self.scrolledtext1.config(state= tk.NORMAL)
            self.scrolledtext1.delete("1.0", tk.END)
            self.scrolledtext1.insert("1.0", contenido)
            self.scrolledtext1.config(state= tk.DISABLED)
            
            self.label_lineas.config(text= f"Lineas: {num_lineas}")
            self.label_palabras.config(text= f"Palabras: {num_palabras}")
            self.label_caracteres.config(text= f"Caracteres: {num_caracteres}")

#########################   Main    ################################

aplicacion = Aplicacion()