from src.modelo import Personaje

class El_Defectuoso(Personaje):
    
    def __init__(self, nombre, vida, daño, defensa):
        super().__init__(nombre, vida, daño, defensa)
        self.orbes = 0
        self.mana = 0

    def atacar(self, Personaje):
        if self.estado() == True:
            #si el personaje esta vivo, pasa a la siguiente condicion
            if Personaje.estado() == True:
                #si el oponente tiene vida imprime que X ataca a otro X y pasa a otra condicion
                print(f"{self.nombre} ataca a {Personaje.nombre}\n")
                if self.orbes == 0:
                    #si el personaje NO tiene orbes pasa a la siguiente condicion
                    if self.mana < 3:
                        #si el personaje tiene menos de 3 manas, este aumenta en 1 y realiza el ataque
                        self.mana += 1
                        daño_total = self.daño - Personaje.defensa

                        if daño_total > 0:
                            #si el daño total es mayor a cero entonces se le resta el daño total a la vida del oponente
                            print(f"\n{Personaje.nombre} ah recibido {daño_total} puntos de daño\n")
                            Personaje.vida -= daño_total
                        else:
                            #en caso de que el daño_total sea igual o menor a 0 entonces no se hace daño
                            print(f"{Personaje.nombre} no ha recibido daño\n")
                    else:
                        #en caso de tener 3 de mana, se activa su ataque especial
                        print(f"{self.nombre} ha activado su ataque especial\n")
                        self.ataque_especial(Personaje)
                else:
                    #en caso de tener orbes, entonces aumenta su fuerza en 5 y sus siguientes 3 ataques son mas fuertes
                    daño_total = (self.daño + 5) - Personaje.defensa
                    self.orbes -= 1
                    if daño_total > 0:
                        #si daño total es mayor a cero entonces el oponente recibe el ataque y baja su vida
                        print(f"\n{Personaje.nombre} ah recibido {daño_total} puntos de daño\n")
                        Personaje.vida -= daño_total
                    else:
                        #en caso de que el daño_total sea igual o menor a 0 entonces no se hace daño
                        print(f"{Personaje.nombre} no ha recibido daño\n")
            else:
                print(f"No puedes seguir atacando. {Personaje.nombre} esta muerto")
        else:
            print(f"{self.nombre} no puede atacar desde la tumba\n")
            return False
       
    def estadisticas(self):
            #muestra estadisticas del personaje incliyendo sus ORBES 
            if self.estado() == True:
                print(f"Nombre= {self.nombre}\nVida ={self.vida}\nDaño = {self.daño}\nMana = {self.mana}\nOrbes={self.orbes}\n")
            else:
                print(f"Nombre= {self.nombre}\n ¡MUERTO!\n") 

    def ataque_especial(self, Personaje):
        #su ataque especial activa 3 orbes que seran lanzados al enemigo durante los sigueintes 3 turnos (esto no genera mas mana)
        self.orbes = 3
        self.mana -= 3
    