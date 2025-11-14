# TP 8 Ejercicio 13
def buscarclave(diccionario: dict, valor) -> list:
    """
    Devuelve una lista con las claves cuyo valor coincide
    con el valor buscado.
    """
    return [clave for clave, v in diccionario.items() if v == valor]


def main():
    # Diccionario de ejemplo
    datos = {
        "A": 10,
        "B": 20,
        "C": 10,
        "D": 30,
        "E": 20
    }

    print("Diccionario:", datos)
    valor = input("\nIngresa un valor a buscar: ")

    # Convertimos a número si corresponde
    if valor.isdigit():
        valor = int(valor)

    claves = buscarclave(datos, valor)

    if claves:
        print(f"\nClaves que contienen el valor {valor}: {claves}")
    else:
        print(f"\nNo existe ninguna clave cuyo valor sea {valor}.")


if __name__ == "__main__":
    main()
