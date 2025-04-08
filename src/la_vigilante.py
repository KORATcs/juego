from modelo import Personaje

class La_vigilante(Personaje):
    #clase "la vigilante"
    def ataque_especial(self, Personaje):
        self.__daño = self.__daño * 2
        print(f"{self._nombre} ha duplicado su ataque a {self.__daño}\n")
        
        if self.__daño > 0:
            Personaje.__vida -= self.__daño
            self.__mana = 0
            print(f"{Personaje._nombre} recibio {self.__daño} puntos de daño")
        return super().ataque_especial()