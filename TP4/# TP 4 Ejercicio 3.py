# TP 4 Ejercicio 3
def separar_claves(clave_maestra: str) -> tuple:
    """
    Recibe la clave maestra (cadena de dígitos) y devuelve dos cadenas:
    (clave1, clave2) donde clave1 son los dígitos en posiciones impares
    y clave2 los dígitos en posiciones pares (numeración desde 1, izquierda).
    Precondición: clave_maestra contiene sólo caracteres '0'..'9' y no está vacía.
    Poscondición: retorna dos cadenas (pueden ser vacías si no hay dígitos en una paridad).
    """
    c1 = []
    c2 = []
    for idx, ch in enumerate(clave_maestra, start=1):
        if idx % 2 == 1:
            c1.append(ch)
        else:
            c2.append(ch)
    return "".join(c1), "".join(c2)


def main() -> None:
    clave = input("Ingrese la clave maestra (solo dígitos): ").strip()
    if not clave.isdigit() or clave == "":
        print("Entrada inválida. Ingrese únicamente dígitos.")
        return

    clave1, clave2 = separar_claves(clave)
    print("Clave 1 (posiciones impares):", clave1)
    print("Clave 2 (posiciones pares)  :", clave2)


if __name__ == "__main__":
    main()
