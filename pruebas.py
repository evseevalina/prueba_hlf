
from utils import crear_tableros, crear_barco, colocar_barcos, disparar

# 1. Comprobar las dimensiones del tablero.
tablero = crear_tableros()
assert tablero.shape == (10, 10)
assert (tablero == "_").all()

# 2. Comprobar la longitud de un barco.
barco = crear_barco(4)
assert len(barco) == 4

# 3. Comprobar la colocación de la flota.
tablero = colocar_barcos(crear_tableros())
assert (tablero == "O").sum() == 16

# 4. Comprobar un disparo acertado.
tablero_barcos = crear_tableros()
tablero_disparos = crear_tableros()
tablero_barcos[2, 3] = "O"

resultado = disparar(
    (2, 3), tablero_barcos, tablero_disparos
)

assert tablero_disparos[2, 3] == "X"
assert resultado == "¡Tocado!"

# 5. Comprobar un disparo al agua.
resultado = disparar(
    (0, 0), tablero_barcos, tablero_disparos
)

assert tablero_disparos[0, 0] == "A"
assert resultado == "Agua."

print("Todas las pruebas han pasado correctamente.")

