from modelo import Personaje

class El_Defectuoso(Personaje):
    
    def __init__(self, nombre, vida, daño, defensa):
        super().__init__(nombre, vida, daño, defensa)
        self.__orbes = 0
        self.__mana = 0

    def atacar(self, Personaje):
        if self.estado() == True:
            #si el personaje esta vivo, pasa a la siguiente condicion
            if Personaje.estado() == True:
                #si el oponente tiene vida imprime que X ataca a otro X y pasa a otra condicion
                print(f"{self._nombre} ataca a {Personaje._nombre}\n")
                if self.__orbes == 0:
                    #si el personaje NO tiene orbes pasa a la siguiente condicion
                    if self.get_mana() < 3:
                        #si el personaje tiene menos de 3 manas, este aumenta en 1 y realiza el ataque
                        self.set_mana(1)
                        daño_total = self.get_daño() - Personaje.get_defensa()
                        if daño_total > 0:
                            print(f"\n{Personaje._nombre} ah recibido {daño_total} puntos de daño\n")
                            vida_actual = Personaje.get_vida()
                            Personaje.set_vida(vida_actual - daño_total)
                        else:
                            #en caso de que el daño_total sea igual o menor a 0 entonces no se hace daño
                            print(f"{Personaje._nombre} no ha recibido daño\n")
                    else:
                        print(f"{self._nombre} ha activado su ataque especial\n")
                        self.ataque_especial(Personaje)

                else:
                    daño_total = (self.get_daño()+5) - Personaje.get_defensa()
                    self.__orbes -= 1
                    if daño_total > 0:
                        #si daño total es mayor a cero entonces el oponente recibe el ataque y baja su vida
                        print(f"\n{Personaje._nombre} ah recibido {daño_total} puntos de daño\n")
                        vida_actual = Personaje.get_vida()
                        Personaje.set_vida(vida_actual - daño_total)
                    else:
                        #en caso de que el daño_total sea igual o menor a 0 entonces no se hace daño
                        print(f"{Personaje._nombre} no ha recibido daño\n")
            else:
                print(f"No puedes seguir atacando. {Personaje._nombre} esta muerto")
        else:
            print(f"{self._nombre} no puede atacar desde la tumba\n")
            return False
       
    def estadisticas(self):
            if self.estado() == True:
                print(f"Nombre= {self._nombre}\nVida ={self.get_vida()}\nDaño = {self.get_daño()}\nMana = {self.get_mana()}\nOrbes={self.__orbes}\n")
            else:
                print(f"Nombre= {self._nombre}\n ¡MUERTO!\n") 

    def ataque_especial(self, Personaje):
        self.__orbes = 3
        self.set_mana(-3)
    