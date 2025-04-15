from src.modelo import Personaje

class La_vigilante(Personaje):
    #clase "la vigilante"

    def ataque_especial(self, Personaje):
        #su ataque especial hace que su daño aumente el doble por unica vez, luego vuelve a hacer daño normalmente
        daño_doble = self.daño * 2
        print(f"{Personaje.nombre} ha recibido {daño_doble} puntos de daño del ataque especial\n")
        Personaje.vida -= daño_doble
        self.mana = 0