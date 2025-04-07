from modelo import Personaje, la_vigilante, devorador_del_tiempo
#importo la clase "Personaje" desde el archivo modelo.py 

def main():
    #creacion de los Personajes

    guerrero = la_vigilante ("La Vigilante", 72, 9, 8)
    enemigo = devorador_del_tiempo ("Devorador del Tiempo", 100, 15, 0)

    enemigo.concentrar()
    print("")
    enemigo.atacar(guerrero)
    print("")
    enemigo.atacar(guerrero)
    print("")
    guerrero.atacar(enemigo)
    

if __name__ == "__main__":
    main()