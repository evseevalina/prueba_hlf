import numpy as np

TAMANO = 10
ESLORAS_FLOTA = [4, 3, 3, 2, 2, 2]


def crear_tableros(tamano=TAMANO):
    return np.full((tamano, tamano), "_", dtype=str)


def crear_barco(eslora, tamano=TAMANO):
    orientacion = np.random.choice(["V", "H"])

    if orientacion == "V":
        fila = np.random.randint(0, tamano - eslora + 1)
        columna = np.random.randint(0, tamano)
        return [(fila + i, columna) for i in range(eslora)]

    fila = np.random.randint(0, tamano)
    columna = np.random.randint(0, tamano - eslora + 1)
    return [(fila, columna + i) for i in range(eslora)]


def colocar_barcos(tablero):
    for eslora in ESLORAS_FLOTA:
        while True:
            barco = crear_barco(eslora)

            # Comprobar si todas las posiciones están libres.
            if all(tablero[f, c] == "_" for f, c in barco):
                for f, c in barco:
                    tablero[f, c] = "O"
                break

    return tablero


def disparar(casilla, tablero_barcos, tablero_disparos):
    fila, columna = casilla

    if not (0 <= fila < TAMANO and 0 <= columna < TAMANO):
        return "Coordenadas fuera del tablero."

    if tablero_disparos[fila, columna] != "_":
        return "Ya has disparado en esa casilla."

    if tablero_barcos[fila, columna] == "O":
        tablero_disparos[fila, columna] = "X"
        return "¡Tocado!"

    tablero_disparos[fila, columna] = "A"
    return "Agua."


def quedan_barcos(tablero_barcos, tablero_disparos):
    return np.any(
        (tablero_barcos == "O") & (tablero_disparos != "X")
    )