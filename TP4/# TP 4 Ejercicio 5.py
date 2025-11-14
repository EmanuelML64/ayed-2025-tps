# TP 4 Ejercicio 5
def filtrar_palabras_ciclos(frase: str, N: int) -> str:
    """
    Devuelve las palabras de la frase que tengan N o más caracteres.
    """
    palabras = frase.split()
    resultado = []
    for palabra in palabras:
        if len(palabra) >= N:
            resultado.append(palabra)
    return " ".join(resultado)

def filtrar_palabras_comp(frase: str, N: int) -> str:
    """
    Devuelve las palabras con N o más caracteres.
    
    """
    return " ".join([p for p in frase.split() if len(p) >= N])

def filtrar_palabras_filter(frase: str, N: int) -> str:
    """
    Devuelve las palabras con N o más caracteres.
    
    """
    return " ".join(filter(lambda p: len(p) >= N, frase.split()))


def main() -> None:
    frase = input("Ingrese una frase: ")
    N = int(input("Ingrese la longitud mínima de palabra: "))

    print("\nCon ciclos normales:")
    print(filtrar_palabras_ciclos(frase, N))

    print("\nCon comprensión de listas:")
    print(filtrar_palabras_comp(frase, N))

    print("\nCon filter:")
    print(filtrar_palabras_filter(frase, N))


if __name__ == "__main__":
    main()
