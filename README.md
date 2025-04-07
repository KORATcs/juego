# 🧙‍♂️ Sistema de Combate RPG en Python

Este proyecto simula un sistema de combate entre personajes en un juego RPG. Utiliza programación orientada a objetos con herencia, métodos personalizados, y una lógica de batalla simple pero extendible.

## 📁 Estructura del Proyecto

proyecto/ 
│ ├── modelo.py # Contiene la lógica de las clases y personajes 
├── main.py # Simula el combate entre personajes 
└── README.md # Este archivo

## 🚀 Cómo Ejecutar

1. Asegúrate de tener Python 3 instalado.
2. Descarga o clona este proyecto.
3. Ejecuta el archivo `main.py` desde la terminal:

```bash
python main.py

🧩 Clases y Funcionalidades
Personaje

Clase base que contiene:

    atacar(Personaje): Ataca a otro personaje y suma 1 de maná.

    ataque_especial(): Acción única que varía según el tipo de personaje (debe sobreescribirse).

    concentrar(): Gana 2 de maná al instante.

    estado(): Verifica si está vivo o muerto.

    estadisticas(): Muestra su nombre, vida, daño y maná.

🧙‍♀️ Personajes
la_vigilante (subclase de Personaje)

    Ataque especial: Duplica su daño al alcanzar 3 de maná.

devorador_del_tiempo (subclase de Personaje)

    Ataque especial: Aumenta su defensa en 2 puntos al alcanzar 3 de maná.

⚔️ Mecánica del Juego

    Los personajes atacan si están vivos.

    Cada ataque suma 1 de maná.

    Al llegar a 3 de maná, el personaje debe usar su ataque especial.

    El daño total se calcula como:
    daño_total = daño_atacante - defensa_objetivo

    Si el daño es menor o igual a 0, no se inflige daño.

    Si la vida llega a 0, el personaje se considera muerto y no puede seguir combatiendo.

🧪 Ejemplo de Uso

from modelo import Personaje, la_vigilante, devorador_del_tiempo

guerrero = la_vigilante("La Vigilante", 20, 9, 8)
enemigo = devorador_del_tiempo("Devorador del Tiempo", 50, 15, 0)

guerrero.atacar(enemigo)

💡 Mejoras Futuras

    Más personajes con habilidades únicas.

    Combates por turnos.

    Interfaz gráfica (GUI o consola interactiva).

    Sistema de niveles y experiencia.
