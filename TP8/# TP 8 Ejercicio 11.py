# TP 8 Ejercicio 11
def contar_vocales(palabra: str) -> dict:
    """
    Recibe una palabra y devuelve un diccionario con la cantidad
    de cada vocal encontrada.
    """
    vocales = "aeiou"
    conteo = {v: 0 for v in vocales}

    for letra in palabra.lower():
        if letra in conteo:
            conteo[letra] += 1

    return {v: c for v, c in conteo.items() if c > 0}


def main():
    frase = input("Ingresa una frase: ")

    palabras = frase.split()

    for palabra in palabras:
        resultado = contar_vocales(palabra)

        if resultado:  
            print(f"\nPalabra: {palabra}")
            print("Vocales:", resultado)
        else:
            print(f"\nPalabra: {palabra} (no tiene vocales)")


if __name__ == "__main__":
    main()
