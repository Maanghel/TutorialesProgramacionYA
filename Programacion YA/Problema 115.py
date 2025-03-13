"""
Modificar el problema que desplaza un cuadrado con las teclas de flechas de tal modo que la figura 
no pueda salir del espacio definido para el Canvas.
Para saber la posición actual de una figura la clase Canvas cuenta con el método 'coords':
        x1, y1, x2, y2 = self.canvas1.coords(self.cuadrado)
"""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.canvas1 = tk.Canvas(self.ventana1, width= 600, height= 400, background= "black")
        self.canvas1.grid(column= 0, row= 0)
        self.cuadrado = self.canvas1.create_rectangle(150, 10, 200, 60, fill= "red") # Crea un rectangulo
        self.ventana1.bind("<KeyPress>", self.presion_tecla) # Detecta el evento de presionar una tecla
        self.ventana1.mainloop()
    
    def presion_tecla(self, evento):
        # Funcion que realiza que el cuadrado se mueva segun la key que se presione
        x1, y1, x2, y2 = self.canvas1.coords(self.cuadrado) # Obtiene las cordenadas actual de la figura
        if evento.keysym == 'Right':
            if x2 + 10 <= 600:
                self.canvas1.move(self.cuadrado, 10, 0)
        if evento.keysym == 'Left':
            if x1 - 10 >= 0:
                self.canvas1.move(self.cuadrado, -10, 0)
        if evento.keysym == 'Down':
            if y2 + 10 <= 400:
                self.canvas1.move(self.cuadrado, 0, 10)
        if evento.keysym == 'Up':
            if y1 - 10 >= 0:
                self.canvas1.move(self.cuadrado, 0, -10)

#########################   Main    ################################

aplicacion1=Aplicacion()