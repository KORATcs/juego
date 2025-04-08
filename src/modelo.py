class Personaje:
    
    def __init__ (self, nombre, vida, daño, defensa):
        #metodo que inicializa la clase "Personaje"
        self._nombre = nombre
        self.__vida = vida
        self.__daño = daño
        self.__defensa = defensa
        self.__mana = 0

    def atacar (self, Personaje):
        #funcion que permite que un Personaje haga daño a otro Personaje
        if self.estado() == True:
            #si el personaje que va a atacar esta con vida, ataca a su oponente y suma 1 mana 
            #el mana es una energia que va aumentando de a 1 por cada ataque, si junta 3 obligatoriamente
            #debe utilizar su ataque especial
            if Personaje.estado() == True:
            
                print(f"{self._nombre} ataca a {Personaje._nombre}\n")

                if self.__mana < 3:
                    self.__mana += 1
                    daño_total = self.__daño - Personaje.__defensa  

                    if daño_total > 0:
                        print(f"\n{Personaje._nombre} ah recibido {daño_total} puntos de daño\n")
                        Personaje.__vida -= daño_total
                    else:
                        #en caso de que el daño_total sea igual o menor a 0 entonces no se hace daño
                        print(f"{Personaje._nombre} no ha recibido daño\n")
                else:
                    print(f"{self._nombre} ha activado su ataque especial\n")
                    self.ataque_especial(Personaje)
            else:
                print(f"No puedes seguir atacando. {Personaje._nombre} esta muerto")
        else:
            print(f"{self._nombre} no puede atacar desde la tumba\n")
            return False

    def ataque_especial (self):
        #metodo que permite que un Personaje realice una accion especial (distinta por cada Personaje)
        #este metodo solo tendra la informacion necesaria dentro de cada clase de personaje especifico
        pass

    def concentrar (self):
        #al concentrarse el personaje recibe 2 de mana al instante, lo que le permite mas pronto realizar un ataque especial
        print(f"{self._nombre} concentró su energia y ganó 2 maná\n")
        self.__mana += 2
    
    def estado (self):
        #muestro si el personaje esta vivo o muerto
        if self.__vida > 0:
            return True
        else:
            return False

    def estadisticas (self):
        #muestra nombre, vida, daño y mana disponible del personaje que esta combatiendo.
        #en caso de estar muerto, se mostrara solo el nombre.
        if self.estado() == True:
            print(f"Nombre= {self._nombre}\nVida ={self.__vida}\nDaño = {self.__daño}\nMana = {self.__mana}\n")
        else:
            print(f"Nombre= {self._nombre}\n ¡MUERTO!\n") 

    #GETTERS Y SETTERS para que sean accesibles los siguientes atributos desde las subclases
    def get_vida(self):
        return self.__vida
    
    def set_vida(self, nueva_vida):
        self.__vida += nueva_vida

    def get_daño(self):
        return self.__daño
    
    def set_daño(self, nuevo_daño):
        self.__daño += nuevo_daño

    def get_defensa(self):
        return self.__defensa
    
    def get_mana(self):
        return self.__mana
    
    def set_mana(self, nuevo_mana):
        self.__mana += nuevo_mana