import numpy as np

from utils import (
    crear_tableros,
    colocar_barcos,
    disparar,
    quedan_barcos,
    TAMANO,
)


def mostrar_tablero(tablero):
    print("   " + " ".join(f"{i:2}" for i in range(TAMANO)))
    for i, fila in enumerate(tablero):
        print(f"{i:2} " + "  ".join(fila))


def pedir_coordenadas(tablero_disparos):
    while True:
        try:
            fila = int(input("Fila (0-9): "))
            columna = int(input("Columna (0-9): "))

            if not (0 <= fila < TAMANO and 0 <= columna < TAMANO):
                print("Introduce coordenadas entre 0 y 9.")
                continue

            if tablero_disparos[fila, columna] != "_":
                print("Ya has disparado ahí. Prueba otra casilla.")
                continue

            return fila, columna

        except ValueError:
            print("Introduce números enteros.")


def main():
    barcos_jugador = colocar_barcos(crear_tableros())
    disparos_jugador = crear_tableros()

    barcos_maquina = colocar_barcos(crear_tableros())
    disparos_maquina = crear_tableros()

    print("\n¡Bienvenido a Hundir la Flota!")

    while True:
        print("\nTU TABLERO")
        mostrar_tablero(barcos_jugador)

        print("\nTUS DISPAROS CONTRA LA MÁQUINA")
        mostrar_tablero(disparos_jugador)

        fila, columna = pedir_coordenadas(disparos_jugador)

        resultado = disparar(
            (fila, columna), barcos_maquina, disparos_jugador
        )
        print("\nTu disparo:", resultado)

        if not quedan_barcos(barcos_maquina, disparos_jugador):
            print("¡Enhorabuena! Has hundido toda la flota.")
            break

        # Turno de la máquina.
        while True:
            f = np.random.randint(TAMANO)
            c = np.random.randint(TAMANO)

            if disparos_maquina[f, c] == "_":
                break

        resultado = disparar(
            (f, c), barcos_jugador, disparos_maquina
        )
        print(f"La máquina dispara a ({f}, {c}): {resultado}")

        if not quedan_barcos(barcos_jugador, disparos_maquina):
            print("La máquina ha hundido toda tu flota. ¡Fin de la partida!")
            break


if __name__ == "__main__":
    main()
