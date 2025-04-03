"""
Desarrollar un programa que implemente una clase llamada Jugador.
Definir como atributos su nombre y puntaje.
Codificar el método especial __str__ que retorne el nombre y si es principiante (menos de 1000 puntos) o experto (1000 o más puntos)
"""

class Jugador:
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
    
    def __str__(self):
        # Funcion usando el metodo especial que se llama al usar print
        cadena = f"\nJugador: {self.nombre}\nPuntaje: {str(self.puntaje)}"
        if self.puntaje < 1000:
            cadena += "\nTipo: Principiante"
        else:
            cadena += "\nTipo: Experto"
        return cadena

#########################   Main    ################################

jugador1 = Jugador("Manuel", 500)
jugador2 = Jugador("Juan", 700)
jugador3 = Jugador("Julia", 1500)

print(jugador1)
print(jugador2)
print(jugador3)