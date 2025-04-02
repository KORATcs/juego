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
        if Personaje.estado == True:
            if self.mana < 3:
                self.mana += 1
                daño_total = self.daño-Personaje.defensa  

                if daño_total <= 0:
                    return "no ha recibido daño"
                
                return "f{self.personaje.nombre} ha recibido {daño_total} de daño"
            else:
                self.ataque_especial()
        else:
            return False

    def ataque_especial (self):
        #funcion que permite que un Personaje realice una accion especial (distinta por cada Personaje)
        #esta funcion solo tendra la informacion necesaria dentro de cada clase de personaje especifico
        pass

    def concentrar (self):
        #al concentrarse el personaje recibe 2 de mana al instante, lo que le permite mas pronto realizar un ataque especial
        self.mana + 2
    
    def estado (self):
        #muestro si el personaje esta vivo o muerto
        if Personaje.vida > 0:
            return True
        else:
            return False

    def estadisticas (self):
        #muestra nombre, vida, daño y mana disponible del personaje que esta combatiendo.
        #en caso de estar muerto, se mostrara solo el nombre.
        if Personaje.estado == True:
            print("estadisticas")
            return "Nombre = f{self.nombre}\n Vida = {self.vida}\n Daño = {self.daño}\n Mana = {self.mana}"
        else:
            return "Nombre = f{self.nombre}\n --sin estadisticas--"
        
class la_vigilante(Personaje):
    #
    def ataque_especial(self):
        return super().ataque_especial()
    
class devorador_del_tiempo(Personaje):
    def ataque_especial(self):
        return super().ataque_especial()