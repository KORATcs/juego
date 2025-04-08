from modelo import Personaje

class La_Silenciosa(Personaje):
    
    def ataque_especial(self, Personaje):
        self.__daño += 1
        print(f"{self._nombre} aumento su daño en 1\n")

        self.__mana = 0
        return super().ataque_especial()