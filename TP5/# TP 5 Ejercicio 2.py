# TP 5 Ejercicio 2
def sumar_cadenas(cad1: str, cad2: str) -> float:
    """
    Suma dos numeros reales representados como cadenas de texto y devuelve el resultado.
    Devuelve -1 si alguna de las cadenas no contiene un numero válido.

    Precondición:
    Ambas cadenas deben representar numeros reales validos.
    Poscondición:
    Devuelve la suma como numero real, o -1 si alguna conversión falla.
    """
    try:
        num1 = float(cad1)
        num2 = float(cad2)
        return num1 + num2
    except ValueError:
        return -1


def main() -> None:
    """
    Prueba la función sumar_cadenas pidiendo dos entradas al usuario y mostrando el resultado.

    Precondicion:
    El usuario debe ingresar dos cadenas representando numeros reales.
    Poscondicion:
    Muestra la suma si ambas son validas o -1 si hubo error en la conversión.
    """
    cad1 = input("Ingrese el primer numero: ")
    cad2 = input("Ingrese el segundo numero: ")
    resultado = sumar_cadenas(cad1, cad2)

    if resultado == -1:
        print("Error: alguna de las cadenas no es un numero valido.")
    else:
        print(f"La suma es: {resultado}")


if __name__ == "__main__":
    main()
