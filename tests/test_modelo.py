#Implementación de Pruebas Unitarias
#✅ Todas las pruebas deben implementarse en la carpeta tests/.
#✅ Se deben probar todos los métodos de la clase principal.
#✅ Cada prueba debe verificar el comportamiento esperado y casos límite.
#✅ Ejemplo de casos límite:
#Recibir daño negativo (¿qué sucede?).
#Ataque con defensa mayor al daño (¿recibe daño o no?).
#Vida en 1 HP y recibir daño (¿muere correctamente?

import unittest
from src.modelo import Personaje, La_vigilante, Devorador_del_tiempo

class TestPersonajes(unittest.TestCase):

    def setUp(self):
        #Configuración inicial antes de cada prueba, cada atributo es un personaje que voy a usar en las pruebas
        self.guerrero = La_vigilante("La Vigilante", 10, 3, 1)
        self.enemigo = Devorador_del_tiempo("Vigilante del Tiempo", 12, 4, 2)
        self.danio_cero = La_vigilante("SinDanio", 1, 0, 0)

    def test_atacar(self):
        #verifica que el ataque reduzca la vida del enemigo correctamente
        self.guerrero.atacar(self.enemigo)
        self.assertEqual(self.enemigo.vida, 11)




    def test_ataque_especial(self):
        pass

    def test_concentrar(self):
        pass

    def test_estado(self):
        pass

    def test_estadisticas(self):
        pass

