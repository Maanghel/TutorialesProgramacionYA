"""
Plantear una clase llamada Jugador.
Definir en la clase Jugador los atributos nombre y puntaje, y los métodos __init__, imprimir y pasar_tiempo (que debe reducir en uno la variable de clase).
Declarar dentro de la clase Jugador una variable de clase que indique cuantos minutos falta para el fin de juego (iniciarla con el valor 30)
Definir en el bloque principal dos objetos de la clase Jugador.
Reducir dicha variable hasta llegar a cero.
"""

class Jugador:
    
    tiempo_juego = 30
    
    def __init__(self, nombre, puntuaje):
        self.nombre = nombre
        self.puntuaje = puntuaje
    
    def imprimir(self):
        print(f"\nJugador: {self.nombre}")
        print(f"Puntuaje: {self.puntuaje}")
        print(f"El juego finaliza en {Jugador.tiempo_juego} minutos.")
    
    def pasar_tiempo(self):
        Jugador.tiempo_juego -= 1

#########################   Main    ################################

jugador1 = Jugador("Manuel", 500)
jugador2 = Jugador("Maria", 700)
while Jugador.tiempo_juego > 0:
    jugador1.imprimir()
    jugador2.imprimir()
    jugador1.pasar_tiempo()