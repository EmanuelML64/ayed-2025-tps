# TP 5 Ejercicio 3
def nombre_mes(numero: int) -> str:
    """
    Devuelve el nombre del mes correspondiente al numero recibido.
    Devuelve una cadena vacia si el numero no corresponde a un mes válido.

    Precondicion:
    El parametro debe ser un numero entero entre 1 y 12.
    Poscondicion:
    Devuelve el nombre del mes o una cadena vacia si el numero es invalido.
    """
    try:
        meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        
        return meses[numero - 1]
    except (IndexError, TypeError):
        return ""


def main() -> None:
    """
    Permite probar la funcion nombre_mes solicitando un numero al usuario y mostrando el resultado.

    Precondicion:
    El usuario debe ingresar un numero entero.
    Poscondicion:
    Muestra el nombre del mes correspondiente o un mensaje de error si es invalido.
    """
    try:
        numero = int(input("Ingrese el numero del mes (1-12): "))
        mes = nombre_mes(numero)
        if mes == "":
            print("Número de mes invalido.")
        else:
            print(f"El mes es: {mes}")
    except ValueError:
        print("Error: debe ingresar un numero entero.")


if __name__ == "__main__":
    main()
