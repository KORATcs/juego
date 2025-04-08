from devorador_del_tiempo import Devorador_del_tiempo
from la_vigilante import La_vigilante
from la_silenciosa import La_Silenciosa
from el_defectuoso import El_Defectuoso
from el_blindado import El_Blindado

#importo la clase "Personaje" desde el archivo modelo.py 

def main():
    #creacion de los Personajes

    monje = La_vigilante ("La Vigilante", 72, 9, 6)
    enemigo = Devorador_del_tiempo ("Devorador del Tiempo", 100, 15, 0)
    picaro = La_Silenciosa ("La Silenciosa", 70, 5, 2)
    mago = El_Defectuoso ("El Defectuoso", 65, 5, 0)
    guerrero = El_Blindado ("El blindado", 40, 9, 8)

if __name__ == "__main__":
    main()