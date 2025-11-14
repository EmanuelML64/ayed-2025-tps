# TP 8 Ejercicio 4
from typing import Tuple


def encajan(ficha1: Tuple[int, int], ficha2: Tuple[int, int]) -> bool:
    """
    Determina si dos fichas de dominó encajan.
    
    Dos fichas encajan si comparten al menos un número.
    
    Parámetros
    
    ficha1 : Tuple[int, int]
        Primera ficha de dominó.
    ficha2 : Tuple[int, int]
        Segunda ficha de dominó.
    
    Retorna
    
    bool
        True si las fichas encajan, False en caso contrario.
    
    Ejemplo
    
    encajan((3, 4), (5, 4)) -> True
    """
    

    set1 = set(ficha1)
    set2 = set(ficha2)


    return len(set1 & set2) > 0

def main():
    ejemplos = [
        ((3, 4), (5, 4)),
        ((2, 6), (1, 5)),
        ((0, 0), (0, 3)),
        ((1, 3), (3, 1)),
        ((6, 2), (4, 6))
    ]
    
    for f1, f2 in ejemplos:
        print(f"¿Encajan {f1} y {f2}? -> {encajan(f1, f2)}")


if __name__ == "__main__":
    main()
