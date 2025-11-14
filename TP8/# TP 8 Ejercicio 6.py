# TP 8 Ejercicio 6
import string
from typing import List


def limpiar_palabra(palabra: str) -> str:
    """
    Elimina signos de puntuación alrededor de una palabra.

    Parámetros
    
    palabra : str
    Palabra que puede contener signos de puntuación.

    Retorna
    
    str
    Palabra limpia sin signos de puntuación.
    """
    return palabra.strip(string.punctuation)


def procesar_frase(frase: str) -> List[str]:
    """
    Recibe una frase, elimina palabras repetidas y las ordena por longitud.

    Parámetros
    
    frase : str
    Cadena ingresada por el usuario.

    Retorna
    
    List[str]
    Lista de palabras únicas, limpias y ordenadas por longitud.
    """
    palabras = frase.split()

    # Limpiar puntuación y convertir a minúsculas
    palabras_limpias = {limpiar_palabra(p).lower() for p in palabras if limpiar_palabra(p)}

    # Ordenar por longitud
    return sorted(palabras_limpias, key=len)


def main():
    frase = input("Ingresa una frase: ")
    resultado = procesar_frase(frase)
    
    print("\nPalabras unicas ordenadas por longitud:")
    for palabra in resultado:
        print(palabra)


if __name__ == "__main__":
    main()
