from modelo import Personaje, la_vigilante, devorador_del_tiempo
#importo la clase "Personaje" desde el archivo modelo.py 

def main():
    #creacion de los Personajes

    guerrero = la_vigilante ("La Vigilante", 20, 9, 8)
    enemigo = devorador_del_tiempo ("Devorador del Tiempo", 0, 15, 0)

    guerrero.atacar(enemigo)
    
    
if __name__ == "__main__":
    main()