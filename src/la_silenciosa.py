from src.modelo import Personaje

class La_Silenciosa(Personaje):
    
    def ataque_especial(self, Personaje):
        #aumenta su daño en 1(es acumulativo) y reinicia su mana luego de activar su ataque especial
        self.daño += 1
        print(f"{self.nombre} aumento su daño en 1\n")

        self.mana = 0
        return super().ataque_especial()