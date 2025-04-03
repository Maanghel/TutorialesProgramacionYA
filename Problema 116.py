"""
Disponer de un boton y mostrar al azar una de las tres cartas del problema anterior.
Cada vez que se presione el boton generar un valor aleatorio y a partir de dicho valor
mostrar una carta
"""

import random
import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        
        self.canvas1 = tk.Canvas(self.ventana1, width= 700, height= 500, background= "black" )
        self.canvas1.grid(column= 0, row= 0)
        self.archivo1 = tk.PhotoImage(file= "Programacion YA\carta1.png") # Carga una imagen en una variable
        self.archivo2 = tk.PhotoImage(file= "Programacion YA\carta2.png")
        self.archivo3 = tk.PhotoImage(file= "Programacion YA\carta3.png")
        
        self.button1 = ttk.Button(self.ventana1, text= "Mostrar carta aleatoria", command= self.mostrar_carta)
        self.button1.grid(column = 0, row= 0, sticky= "s", pady= 10)
        
        self.ventana1.mainloop()
    
    def mostrar_carta(self):
        # Funcion que muestra una carta aleatoria
        opcion = random.randint(1, 3) # Genera un numero aleatorio del 1 al 3
        
        if opcion == 1:
            self.canvas1.create_image(240, 100, image= self.archivo1, anchor= "nw") # Crea una imagen con la imagen guardada en el archivo correspondiente
        elif opcion == 2:
            self.canvas1.create_image(240, 100, image= self.archivo2, anchor= "nw")
        else:
            self.canvas1.create_image(240, 100, image= self.archivo3, anchor= "nw")

#########################   Main    ################################

aplicacion = Aplicacion()