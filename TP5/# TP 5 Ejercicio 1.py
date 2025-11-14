# TP 5 Ejercicio 1
def ingresar_natural() -> int:
    """
    Solicita al usuario ingresar un número natural (entero positivo) y valida el ingreso
    utilizando excepciones. Muestra mensajes de error especificos por cada tipo de entrada invalida.

    Precondicion:
    El usuario debe ingresar un valor que pueda convertirse en numero entero y sea mayor que cero.
    Poscondicion:
    Devuelve el numero natural ingresado correctamente por el usuario.
    """
    while True:
        try:
            entrada = input("Ingrese un numero natural: ").strip()

            if entrada == "":
                raise ValueError("No se ingreso ningún valor.")

            numero = float(entrada)  

            if not numero.is_integer():
                raise ValueError("El numero ingresado no es un entero.")

            numero = int(numero)

            if numero <= 0:
                raise ValueError("El numero debe ser mayor que cero.")

            return numero

        except ValueError as e:
            print(f" Error: {e}")
        except Exception:
            print(" Error desconocido. Intente nuevamente.")


def main() -> None:
    """
    Prueba la función ingresar_natural solicitando un numero al usuario e imprimiendo
    el resultado valido cuando se ingresa correctamente.

    Precondicion:
        El usuario debe interactuar por teclado.
    Poscondicion:
        Muestra el numero natural ingresado cuando se valida correctamente.
    """
    numero = ingresar_natural()
    print(f" Numero ingresado correctamente: {numero}")


if __name__ == "__main__":
    main()
