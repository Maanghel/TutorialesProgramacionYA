import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Generador de Contraseñas Seguras")
        self.ventana1.geometry("400x250")
        self.ventana1.resizable(False, False)
        
        self.configuracion_contraseña()
        
        self.ventana1.mainloop()
        
    def configuracion_contraseña(self):
        self.frame = ttk.Labelframe(self.ventana1, text= "Configurar Contraseña a generar")
        self.frame.grid(column= 0, row= 0, padx= 5, pady= 5)
        
        self.label1 = ttk.Label(self.frame, text= "Longitud de la contraseña:")
        self.label1.grid(column= 0, row= 0, pady= 5, padx= 5, sticky= "w")
        
        self.entry_longitud = ttk.Entry(self.frame, width= 11)
        self.entry_longitud.insert(0, "12")
        self.entry_longitud.grid(column= 0, row= 0, padx= 5, pady= 5, sticky= "e")
        
        self.var_mayus = tk.BooleanVar(value= True)
        self.var_numeros = tk.BooleanVar(value= True)
        self.var_simbolos = tk.BooleanVar(value= True)
        
        self.checkbutton_mayus = ttk.Checkbutton(self.frame, text= "Incluir mayúsculas", variable= self.var_mayus)
        self.checkbutton_mayus.grid(column= 0, row= 1, padx= 5, pady= 5, sticky= "w")
        self.checkbutton_numeros = ttk.Checkbutton(self.frame, text= "Incluir números", variable= self.var_numeros)
        self.checkbutton_numeros.grid(column= 0, row= 2, padx= 5, pady= 5, sticky= "w")
        self.checkbutton_simbolos = ttk.Checkbutton(self.frame, text= "Incluir símbolos", variable= self.var_simbolos)
        self.checkbutton_simbolos.grid(column= 0, row= 3, padx= 5, pady= 5, sticky= "w")
        
        self.button_generar = ttk.Button(self.frame, text= "Generar Contraseña", command= self.generar_contraseña)
        self.button_generar.grid(column= 0, row= 4, padx= 5, pady= 5)
        
        self.entry_contraseña = ttk.Entry(self.frame, width= 30, state= "readonly", font= ("Arial, 12"))
        self.entry_contraseña.grid(column= 0, row= 5, padx= 5, pady= 5)
    
    def generar_contraseña(self):
        try:
            longitud = int(self.entry_longitud.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido para la longitud.")
            return
        
        incluir_mayus = self.var_mayus.get()
        incluir_numeros = self.var_numeros.get()
        incluir_simbolos = self.var_simbolos.get()
            
        caracteres = string.ascii_lowercase
        if incluir_mayus:
            caracteres += string.ascii_uppercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_simbolos:
            caracteres += string.punctuation
            
        if longitud < 4:
            messagebox.showwarning("Advertencia", "La contraseña debe tener al menos 4 caracteres.")
            return
            
        contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
            
        self.entry_contraseña.config(state= "normal")
        self.entry_contraseña.delete(0, tk.END)
        self.entry_contraseña.insert(0, contraseña)
        self.entry_contraseña.config(state= "readonly")

#########################   Main    ################################

aplicacion = Aplicacion()