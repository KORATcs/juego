from src.devorador_del_tiempo import Devorador_del_tiempo
from src.la_vigilante import La_vigilante
from src.la_silenciosa import La_Silenciosa
from src.el_defectuoso import El_Defectuoso
from src.el_blindado import El_Blindado
from src.modelo import Personaje

#importo la clase "Personaje" desde el archivo modelo.py 

def main():
    #creacion de los Personajes

    monje = La_vigilante ("La Vigilante", 72, 9, 6)
    enemigo = Devorador_del_tiempo ("Devorador del Tiempo", 100, 15, 0)
    picaro = La_Silenciosa ("La Silenciosa", 70, 5, 2)
    mago = El_Defectuoso ("El Defectuoso", 65, 5, 0)
    guerrero = El_Blindado ("El blindado", 40, 9, 8)

    monje.atacar(enemigo)
    enemigo.estadisticas()

    #todos atacan
    monje.atacar(enemigo)
    enemigo.atacar(monje)
    picaro.atacar(mago)
    mago.atacar(guerrero)
    guerrero.atacar(picaro)

    #todos concentran
    monje.concentrar()
    enemigo.concentrar()
    picaro.concentrar()
    mago.concentrar()
    guerrero.concentrar()
    
    #estadisticas
    monje.estadisticas()
    enemigo.estadisticas()
    picaro.estadisticas()
    mago.estadisticas()
    guerrero.estadisticas()

if __name__ == "__main__":
    main()