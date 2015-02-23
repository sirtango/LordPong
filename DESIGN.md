Diseño de LordPong
==================

### Sobre el Juego

- Un juego PONG de forma vertical,
- de un solo jugador contra una IA,
- con varios niveles,
- una historia por nivel,
- ...

### Técnicamente

- Desarrollado en Python usando PyGame,
- Todo el código dentro de un [paquete](https://docs.python.org/2/tutorial/modules.html#packages),
- Implementando `__main__.py` para la ejecución,
- Cada pantalla la definimos como una clase `Scene`,
- Y una clase `SceneManager` que se encarga de cambiar entre pantallas,
- Definimos tres pantallas distintas: *Menu*, *Game* y *Static*,
- ...

### Flujo de Pantallas

```
+------+    level 1    +----------+    level n    +------+
| Menu | ------------> |  Static  | ------------> | Game |
+------+               +----------+               +------+
  |                     ^    ^   ^                  |  |
  |       credits       |    |   |     level n+1    |  |
  `---------------------´    |   `------------------´  |
                             |    pause / game over    |
                             `-------------------------´
```
