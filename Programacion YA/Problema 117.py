"""
Crear 100 cuadrados de color rojo y disponerlos en el control Canvas 
en posiciones aleatorias. Permitir desplazar con el mouse cualquiera de los cuadrados.
"""

import random
import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        
        self.canvas1 = tk.Canvas(self.ventana1, width= 1080, height= 800, background= "black")
        self.canvas1.grid(column= 0, row= 0)
        self.crear_cuadrados()
        
        self.canvas1.tag_bind("move", "<ButtonPress-1>", self.presion_boton)
        self.canvas1.tag_bind("move", "<Button1-Motion>", self.mover)
        self.cuadrado_seleccionado = None
        self.ventana1.mainloop()
    
    def crear_cuadrados(self):
        for x in range(100):
            x1 = random.randint(1, 1080)
            y1 = random.randint(1, 800)
            self.canvas1.create_rectangle(x1, y1, x1 + 20, y1 + 20,  fill= "red", tag= "move")
    
    def presion_boton(self, event):
        cuadrado = self.canvas1.find_withtag(tk.CURRENT)
        self.cuadrado_seleccionado = (cuadrado, event.x, event.y)
    
    def mover(self, event):
        x, y = event.x, event.y
        
        cuadrado, x1, y1 = self.cuadrado_seleccionado
        self.canvas1.move(cuadrado, x - x1, y - y1)
        self.cuadrado_seleccionado = (cuadrado, x, y)

#########################   Main    ################################

aplicacion = Aplicacion()