class Personaje:

    def __init__ (self, nombre, vida, daño, defensa):
        #metodo que inicializa la clase "Personaje"
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
        self.defensa = defensa
        self.mana = 0

    def atacar (self, Personaje):
        #funcion que permite que un Personaje haga daño a otro Personaje
        if self.estado() == True:
            #si el personaje que va a atacar esta con via, se verifica despues que el oponente tenga vida
            #el mana es una energia que va aumentando de a 1 por cada ataque, si junta 3 obligatoriamente
            #debe utilizar su ataque especial
            if Personaje.estado() == True:
                #si el oponente esta vivo, entonces comienza el combate
                print(f"{self.nombre} ataca a {Personaje.nombre}\n")
                
                if self.mana < 3:
                    #si el mana es menor a 3, se suma 1 mana y se calcula el daño total que hara un personaje a otro
                    self.mana += 1
                    daño_total = self.daño - Personaje.defensa  

                    if daño_total > 0:
                        #si el daño causado es mayor a 0 entonces se le resta el daño total a la vida del oponente
                        print(f"\n{Personaje.nombre} ah recibido {daño_total} puntos de daño\n")
                        Personaje.vida -= daño_total
                    else:
                        #en caso de que el daño_total sea igual o menor a 0 entonces no se hace nada
                        print(f"{Personaje.nombre} no ha recibido daño\n")
                else:
                    #en caso de que el mana sea igual a 3, se activa la habilidad especial (que cambia segun el personaje)
                    print(f"{self.nombre} ha activado su ataque especial\n")
                    self.ataque_especial(Personaje)
            else:
                #en caso de que el oponente este muerto, se imprimira un mensaje de que no puede seguir el combate
                print(f"No puedes seguir atacando. {Personaje.nombre} esta muerto")
        else:
            #si un personaje esta sin vida, entonces se imprimira un mensaje de que no puede seguri el combate
            print(f"{self.nombre} no puede atacar desde la tumba\n")
            return False

    def ataque_especial (self):
        #metodo que permite que un Personaje realice una accion especial (distinta por cada Personaje)
        #este metodo solo tendra la informacion necesaria dentro de cada clase de personaje especifico
        pass

    def concentrar (self):
        #al concentrarse el personaje recibe 2 de mana al instante, lo que le permite mas pronto realizar un ataque especial
        print(f"{self.nombre} concentró su energia y ganó 2 maná\n")
        self.mana += 2
    
    def estado (self):
        #muestro si el personaje esta vivo o muerto
        if self.vida > 0:
            return True
        else:
            return False

    def estadisticas (self):
        #muestra nombre, vida, daño y mana disponible del personaje que esta combatiendo.
        #en caso de estar muerto, se mostrara solo el nombre y un mensaje de su estado ¡MUERTO!.
        if self.estado() == True:
            print(f"Nombre= {self.nombre}\nVida ={self.vida}\nDaño = {self.daño}\nMana = {self.mana}\n")
        else:
            print(f"Nombre= {self.nombre}\n ¡MUERTO!\n") 