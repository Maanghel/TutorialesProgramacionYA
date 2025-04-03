"""
Disponer tres controles de tipo Radiobutton con las etiquetas 'Rojo', 'Verde' y 'Azul'. 
Cuando se presione un botón cambiar el color de fondo del formulario.
Si consideramos que la variable ventana1 es un objeto de la clase Tk, luego si queremos 
que el fondo sea de color rojo debemos llamar al método configure y en el parámetro bg indicar un string con el color a activar ("red", "green" o "blue"):
            self.ventana1.configure(bg="red")
"""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Prueba")
        
        self.seleccion = tk.IntVar()
        self.radio1 = tk.Radiobutton(self.ventana1, text = "Red", variable = self.seleccion, value = 1)
        self.radio1.grid(column = 0, row = 0)
        self.radio2 = tk.Radiobutton(self.ventana1, text = "Green", variable = self.seleccion, value = 2)
        self.radio2.grid(column = 0, row = 1)
        self.radio3 = tk.Radiobutton(self.ventana1, text = "Blue", variable = self.seleccion, value = 3)
        self.radio3.grid(column = 0, row = 2)
        
        self.button1 = tk.Button(self.ventana1, text = "Cambiar color", command = self.cambiar_color)
        self.button1.grid(column = 0, row = 3)
        
        self.ventana1.mainloop()
    
    def cambiar_color(self):
        # Funcion que cambia el color de la ventana
        if self.seleccion.get() == 1:
            self.ventana1.configure(bg = "red")
        elif self.seleccion.get() == 2:
            self.ventana1.configure(bg = "green")
        elif self.seleccion.get() == 3:
            self.ventana1.configure(bg = "blue")

#########################   Main    ################################

aplicacion = Aplicacion()
