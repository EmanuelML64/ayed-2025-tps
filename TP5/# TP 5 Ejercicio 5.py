# TP 5 Ejercicio 5
import math

def raiz_cuadrada(num: float) -> float:
    """
    Calcula la raiz cuadrada de un numero no negativo.

    Precondicion:
        El parametro num debe ser un número mayor o igual que 0.
    Poscondicion:
        Devuelve la raiz cuadrada de num o -1 si el numero es negativo.
    """
    try:
        if num < 0:
            raise ValueError("No se puede calcular la raiz cuadrada de un numero negativo.")
        return math.sqrt(num)
    except ValueError as e:
        print("Error:", e)
        return -1.0


def main() -> None:
    """
    Solicita un numero al usuario y muestra su raiz cuadrada si es valida.

    Precondición:
    El usuario debe ingresar un número real.
    Poscondición:
    Muestra la raiz cuadrada o un mensaje de error en pantalla.
    """
    try:
        valor = float(input("Ingrese un numero: "))
        resultado = raiz_cuadrada(valor)
        if resultado != -1:
            print(f"La raiz cuadrada de {valor} es {resultado:.2f}")
    except ValueError:
        print("Error: Debe ingresar un valor numerico.")


if __name__ == "__main__":
    main()
