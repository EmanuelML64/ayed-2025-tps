# TP 5 Ejercicio 4
def imprimir_numeros() -> None:
    """
    Imprime los numeros enteros del 1 al 100000.
    Si el usuario presiona Ctrl-C, solicita confirmacion antes de detener el programa.

    Precondicion:
    Ninguna.
    Poscondicion:
    Imprime numeros hasta que el usuario decida detener el programa.
    """
    try:
        for i in range(1, 100001):
            print(i)
    except KeyboardInterrupt:
        respuesta = input("\n¿Desea detener el programa? (s/n): ").strip().lower()
        if respuesta == "s":
            print("Programa detenido por el usuario.")
        else:
            imprimir_numeros()  # Reanuda desde el principio (puede modificarse para continuar)


def main() -> None:
    """
    Ejecuta la funcion principal para imprimir numeros con control de interrupcion.

    Precondicion:
    Ninguna.
    Poscondicion:
    Controla la interrupcion mediante Ctrl-C y confirma con el usuario antes de salir.
    """
    imprimir_numeros()


if __name__ == "__main__":
    main()
