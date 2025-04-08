from modelo import Personaje

class Devorador_del_tiempo(Personaje):
    
    def ataque_especial(self, Personaje):
       #aumenta su defensa en 1. Es acumulativo.
       self.__defensa += 1
       print(f"{self._nombre} aumento su defensa en 1\n")

       self.__mana = 0