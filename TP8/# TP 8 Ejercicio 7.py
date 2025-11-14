# TP 8 Ejercicio 7
from typing import Set

def main() -> None:
    """
    Conjunto inicial {0..9}. Pide numeros al usuario y los elimina con remove().
    Finaliza al ingresar -1. Maneja entradas no numericas y elimina intentos invalidos.
    """
    numeros: Set[int] = set(range(10))
    print("Conjunto inicial:", numeros)

    while True:
        s = input("Numero a eliminar (-1 para salir): ").strip()
        try:
            val = int(s)
        except ValueError:
            print("Ingresa un numero entero.")
            continue

        if val == -1:
            print("Listor.")
            break

        try:
            numeros.remove(val)   # lanza KeyError si no existe
            print("Eliminado. Conjunto:", numeros)
        except KeyError:
            print(f"El valor {val} no esta en el conjunto.")
            
if __name__ == "__main__":
    main()

