from src.modelo import Personaje

class Devorador_del_tiempo(Personaje):
    
    def ataque_especial(self, Personaje):
       #aumenta su defensa en 1. Es acumulativo.
       self.defensa += 1
       print(f"{self.nombre} aumento su defensa en 1\n")

       self.mana = 0