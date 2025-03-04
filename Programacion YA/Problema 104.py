"""
Disponer dos objetos de la clase Button con las etiquetas: "varón" y "mujer",
al presionarse mostrar en la barra de títulos de la ventana la etiqueta del botón presionado.
"""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Prueba")
        
        self.boton1 = tk.Button(self.ventana1, text = "Varon", command = self.presiono_varon)
        self.boton1.grid(column = 1, row = 3)
        
        self.boton2 = tk.Button(self.ventana1, text = "Mujer", command = self.presiono_mujer)
        self.boton2.grid(column = 2, row = 3)
        
        self.ventana1.mainloop()
    
    def presiono_varon(self):
        self.ventana1.title("Varon")
    
    def presiono_mujer(self):
        self.ventana1.title("Mujer")

#########################   Main    ################################

aplicacion = Aplicacion()