# TP 8 Ejercicio 5
from typing import Tuple


def son_ortogonales(v1: Tuple[float, float], v2: Tuple[float, float]) -> bool:
    """
    Determina si dos vectores del plano son ortogonales calculando su producto escalar.

    Parámetros
    
    v1 : Tuple[float, float]
        Primer vector representado por sus componentes (x, y).
    v2 : Tuple[float, float]
        Segundo vector representado por sus componentes (x, y).

    Retorna
    
    bool
        True si los vectores son ortogonales (producto escalar = 0), False en caso contrario.
    """
    producto_escalar = v1[0] * v2[0] + v1[1] * v2[1]
    return producto_escalar == 0


def main():
    print("Pruebas de ortogonalidad:\n")

    ejemplos = [
        ((2, 3), (-3, 2)),
        ((1, 0), (0, 1)),
        ((4, 5), (5, -4)),
        ((1, 2), (2, 1)),
        ((3, 3), (-3, 3)),
    ]

    for v1, v2 in ejemplos:
        print(f"{v1} y {v2} → Ortogonales: {son_ortogonales(v1, v2)}")


if __name__ == "__main__":
    main()
