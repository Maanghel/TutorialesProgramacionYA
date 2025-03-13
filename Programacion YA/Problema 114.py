"""
Implementar un gráfico estadístico de tipo "Barra Porcentual"
"""

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.entrada_datos()
        self.canvas1 = tk.Canvas(self.ventana1, width = 600, height = 400, background = "black")
        self.canvas1.grid(column = 0, row = 1)
        self.ventana1.mainloop()
    
    def entrada_datos(self):
        # Funcion que inserta los widgets para la entrada de datos
        self.lf1 = ttk.LabelFrame(self.ventana1, text = "Partidos Politicos")
        self.lf1.grid(column = 0, row = 0, sticky = "w")
        self.label1 = ttk.Label(self.lf1, text = "Partido A:")
        self.label1.grid(column = 0, row = 0, padx = 5, pady = 5)
        self.datos1 = tk.StringVar()
        self.entry1 = ttk.Entry(self.lf1, width = 30, textvariable = self.datos1)
        self.entry1.grid(column = 1, row = 0, padx = 5, pady = 5)
        self.label2 = ttk.Label(self.lf1, text = "Partido B:")
        self.label2.grid(column = 0, row = 1, padx = 5, pady = 5)
        self.datos2 = tk.StringVar()
        self.entry2 = ttk.Entry(self.lf1, width = 30, textvariable = self.datos2)
        self.entry2.grid(column = 1, row = 1, padx = 5, pady = 5)
        self.label3 = ttk.Label(self.lf1, text = "Partido C:")
        self.label3.grid(column = 0, row = 2, padx = 5, pady = 5)
        self.datos3 = tk.StringVar()
        self.entry3 = ttk.Entry(self.lf1, width = 30, textvariable = self.datos3)
        self.entry3.grid(column = 1, row = 2, padx = 5, pady = 5)
        self.button1 = ttk.Button(self.lf1, text = "Generar Grafico", command = self.generar_grafico)
        self.button1.grid(column = 0, row = 3, columnspan = 2, padx = 5, pady = 5, sticky = "we")
        self.entry1.focus() # Coloca el cursor en el primer entry
    
    def generar_grafico(self):
        # Funcion que genera los graficos
        self.canvas1.delete(tk.ALL) # Borra todo los datos que esten en el canvas en ese momento
        valor1 = int(self.datos1.get())
        valor2 = int(self.datos2.get())
        valor3 = int(self.datos3.get())
        suma = valor1 + valor2 + valor3
        largo1 = valor1 * 500 / suma
        largo2 = valor2 * 500 / suma
        largo3 = valor3 * 500 / suma
        porc1 = valor1 / suma * 100
        porc2 = valor2 / suma * 100
        porc3 = valor3 / suma * 100
        self.canvas1.create_rectangle(10 ,200 ,10 + largo1, 260, fill="red")
        self.canvas1.create_text(50, 220, text = "{0:.2f}".format(porc1) + "%", fill = "white", font = "Arial")
        self.canvas1.create_rectangle(10 + largo1, 200, 10 + largo1 + largo2, 260, fill = "green")
        self.canvas1.create_text(50 + largo1, 220, text = "{0:.2f}".format(porc2) + "%", fill = "white", font = "Arial")
        self.canvas1.create_rectangle(10 + largo1 + largo2, 200, 10 + largo1 + largo2 + largo3, 260, fill = "blue")
        self.canvas1.create_text(50 + largo1 + largo2, 220, text = "{0:.2f}".format(porc3) + "%", fill = "white", font = "Arial")

#########################   Main    ################################

aplicacion = Aplicacion()