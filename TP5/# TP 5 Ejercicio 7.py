# TP 5 Ejercicio 7
import random

def adivinar_numero() -> None:
    """
    Juega con el usuario a adivinar un numero aleatorio entre 1 y 500.

    Precondicion:
        Ninguna.
    Poscondición:
        El programa indica si el numero secreto es mayor o menor y muestra los intentos al acertar.
    """
    numero_secreto = random.randint(1, 500)
    intentos = 0
    print("Pense un numero entre 1 y 500. ¡Adivna!")

    while True:
        try:
            intento = int(input("Ingresa tu numero: "))
            intentos += 1
            if intento < numero_secreto:
                print("El numero secreto es mayor.")
            elif intento > numero_secreto:
                print("El numero secreto es menor.")
            else:
                print(f"¡Correcto! El numero era {numero_secreto}.")
                print(f"Lo lograste en {intentos} intentos.")
                break
        except ValueError:
            intentos += 1
            print("Error: Tenes que ingresar un numero valido.")


def main() -> None:
    """
    Inicia el juego de adivinar el número con manejo de errores.

    Precondicion:
        Ninguna.
    Poscondicion:
        Ejecuta el juego hasta que el usuario adivine el numero.
    """
    adivinar_numero()


if __name__ == "__main__":
    main()
