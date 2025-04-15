from src.modelo import Personaje

class El_Blindado(Personaje):
    
    def ataque_especial(self, Personaje):
        #este metodo hara que el blindado se cure 6 puntos de vida o que haga 6 puntos de daño extra
        if self.vida == 80:
            self.daño += 6
            print(f"{self.nombre} ah aumentado su daño 6 puntos")
            self.mana-=3
        else:
            self.vida += 6
            print(f"{self.nombre} ah aumentado su vida 6 puntos")
            self.mana -= 3