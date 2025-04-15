import unittest
from src.modelo import Personaje
from src.devorador_del_tiempo import Devorador_del_tiempo
from src.la_vigilante import La_vigilante
from src.la_silenciosa import La_Silenciosa
from src.el_defectuoso import El_Defectuoso
from src.el_blindado import El_Blindado

class TestPersonajes(unittest.TestCase):

    def setUp(self):
        #Configuración inicial antes de cada prueba
        self.monje = La_vigilante("La Vigilante", 100, 3, 1)
        self.enemigo = Devorador_del_tiempo("Devorador del Tiempo", 12, 4, 2)
        self.enemigo2 = El_Blindado ("EL blindado", 3, 1, 0)
        self.mago = La_Silenciosa ("Vigilancia", 5, 5, 0)
        self.monje2 = La_vigilante ("bichito", 100, 0, 0)
        self.monje3 = La_Silenciosa ("personaje_de_prueba", 100, 0, 0) #persnaje para hacerle daño
        self.guerrero = El_Defectuoso ("pololo", 10, 10, 0) #no tiene mana cargado
        self.guerrero2 = La_Silenciosa ("sin vida", 0, 0, 0) #tiene vida 0
        self.guerrero3 = La_Silenciosa ("sin_Vida_x2", -50, 0, 0) #tiene vida negativo
        self.devorador = Devorador_del_tiempo ("devorador del tiempo", 10, 1, 0) #habilidad especial
        self.blindado = El_Blindado ("blindado", 60, 1, 0) #habilidad especial: "Blindado" con menos de 80 de vida
        self.blindado2 = El_Blindado ("blindado2", 80, 6, 0) #habilidad especial: "Blindado" con 80 de vida
        self.defectuoso = El_Defectuoso ("defectuoso", 65, 1, 0) #habilidad especial
        self.silenciosa = La_Silenciosa ("silenciosa", 10, 1, 0) #habilidad especial
        self.vigilante = La_vigilante ("vigilante", 10, 5, 0) #habilidad especial

    def test_atacar(self):
        #verifica que el ataque reduzca la vida del enemigo correctamente
        self.monje.atacar(self.enemigo)#golpea 3 puntos de daño
        self.assertEqual(self.enemigo.vida, 11)#bloquea 2 puntos de daño y recibe 1 solo punto dejandolo con 11 de vida

    def test_atacar2(self):
        #verifica que el oponente muera correctamente
        self.monje.atacar(self.enemigo2)#golpea 3 puntos de daño
        self.assertEqual(self.enemigo2.vida, 0)#debe quedar con 0 de vida y morir

    def test_ataque_especial(self):
        #verifica que cargue su ataque especial luego de atacar 3 veces a un oponente
        self.mago.atacar(self.monje2)#+1 mana
        self.mago.atacar(self.monje2)#+2 mana
        self.mago.atacar(self.monje2)#+3 mana

        self.assertEqual(self.mago.mana, 3)

        self.mago.atacar(self.monje2)#ataque especial cargado

        self.assertEqual(self.mago.mana, 0)

    def test_concentrar(self):
        self.guerrero.concentrar() #concentra y gana 2 de mana
        self.assertEqual(self.guerrero.mana, 2) #se le suma 2 de mana

    def test_estado(self):
        self.guerrero2.estado() #consulta su estado, este guerrero tiene 0 de vida
        self.assertEqual(self.guerrero2.estado(), False) #debe dar 0 ya que no tiene vida

        self.guerrero3.estado() #tiene -50 de vida
        self.assertEqual(self.guerrero3.estado(), False) #debe dar False

        self.monje.estado() #tiene 10 de vida
        self.assertEqual(self.monje.estado(), True) #debe dar positivo

    def test_estadisticas(self):
        self.monje.estadisticas()
        self.assertEqual(self.monje.estado(), True) #debe mostrar sus atributos

        self.guerrero2.estadisticas()
        self.assertEqual(self.guerrero2.estado(), False) #imprime mensaje de MUERTO
    
    def test_ataque_especial_Devorador_del_Tiempo(self):
        self.devorador.concentrar() #gana 2 de mana
        self.devorador.atacar(self.enemigo) #gana 1 mana. 
        self.devorador.atacar(self.enemigo) #YA PUEDE ACTIVAR SU HABILIDAD ESPECIAL
        self.assertEqual(self.devorador.defensa, 1) #debe tener +1 defensa

        #OTRA VUELTA PARA VERIFICAR QUE TENGA 2 DE DEFENSA

        self.devorador.concentrar() #gana 2 de mana
        self.devorador.atacar(self.enemigo) #gana 1 mana. 
        self.devorador.atacar(self.enemigo) #YA PUEDE ACTIVAR SU HABILIDAD ESPECIAL
        self.assertEqual(self.devorador.defensa, 2) #debe tener +2 defensa
    
    def test_ataque_especial_El_Blindado(self):
        #PRUEBA: QUE SUME 6 PUNTOS DE VIDA
        self.blindado.concentrar() #aumenta 2 de mana
        self.blindado.atacar(self.guerrero) #aumenta 1 de mana 
        self.blindado.atacar(self.guerrero) #activa su habilidad especial
        self.assertEqual(self.blindado.vida, 66) #debe sumar +6 puntos de vida

        #PRUEBA: QUE SUME 6 PUNTOS DE DAÑO
        self.blindado2.concentrar() #aumenta 2 de mana
        self.blindado2.atacar(self.guerrero) #aumenta 1 de mana 
        self.blindado2.atacar(self.guerrero) #activa su habilidad especial
        self.assertEqual(self.blindado2.daño, 12) #debe sumar +6 puntos de daño
    
    def test_ataque_especial_El_Defectuoso(self):
        #PRUEBA: al activar su ataque especial debe sumar +3 orbes, eventualmente atacar con ellos sin sumar mana
        self.defectuoso.concentrar() #aumenta 2 de mana
        self.defectuoso.atacar(self.monje) #aumenta 1 mana
        self.defectuoso.atacar(self.monje) #activa su habilidad especial
        self.assertEqual(self.defectuoso.orbes, 3) #+3 orbes

        self.defectuoso.atacar(self.monje3) #ataque 1 con orbe
        self.assertEqual(self.monje3.vida, 94) #su vida deberia bajar 6 puntos
        self.defectuoso.atacar(self.monje3) #ataque con 2do orbe
        self.assertEqual(self.monje3.vida, 88) #su vida deberia bajar 6 puntos
        self.defectuoso.atacar(self.monje3) #ataque con su 3er orbe
        self.assertEqual(self.monje3.vida, 82) #su vida deberia bajar 6 puntos
        self.assertEqual(self.defectuoso.mana, 0) #no deberia tener mana
        self.defectuoso.atacar(self.monje3) #ataque normal, ya acabaron sus 3 orbes
        self.assertEqual(self.monje3.vida, 81) #su vida deberia bajar 1 punto
    
    def test_ataque_especial_La_Silenciosa(self):
        #PRUEBA: aumenta su daño +1, es acumulativo

        self.silenciosa.concentrar() #aumenta +2 de mana
        self.silenciosa.atacar(self.monje3) #aumenta +1 de mana
        self.silenciosa.atacar(self.monje3) #activa su habilidad especial
        self.assertEqual(self.silenciosa.daño, 2) #aumenta su daño en +1

        self.silenciosa.concentrar() #aumenta +2 de mana
        self.silenciosa.atacar(self.monje3) #aumenta +1 de mana
        self.silenciosa.atacar(self.monje3) #activa su habilidad especial
        self.assertEqual(self.silenciosa.daño, 3) #aumenta su daño en +1
    
    def test_ataque_especial_La_Vigilante(self):
        self.vigilante.concentrar() #aumenta +2 de mana
        self.vigilante.atacar(self.monje3) #aumenta +2 de mana
        self.vigilante.atacar(self.monje3) #activa su habilidad especial
        self.assertEqual(self.monje3.vida, 85) #aumenta su dalo el doble, hace 25 puntos de daño

        self.vigilante.atacar(self.monje3) #realiza su ataque normal
        self.assertEqual(self.monje3.vida, 80) #le quita 5 puntos de vida
 