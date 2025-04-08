from modelo import Personaje

class El_Blindado(Personaje):
    
    def ataque_especial(self, Personaje):
        #este metodo hara que el blindado se cure 6 puntos de vida o que haga 6 puntos de daño extra
        if self.get_vida() == 80:
            self.set_daño(+6)
            print(f"{self._nombre} ah aumentado su daño 6 puntos")
            self.set_mana(-3)
        else:
            self.set_vida(+6)
            print(f"{self._nombre} ah aumentado su vida 6 puntos")
            self.set_mana(-3)