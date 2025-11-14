# TP 5 Ejercicio 6
def cargar_lista() -> list[int]:
    """
    Carga una lista de numeros enteros ingresados por el usuario, finalizando con -1.

    Precondición:
        El usuario debe ingresar valores enteros, finalizando con -1.
    Poscondición:
        Devuelve una lista con los numeros ingresados, excluyendo el -1.
    """
    lista = []
    while True:
        try:
            num = int(input("Ingrese un numero (-1 para terminar): "))
            if num == -1:
                break
            lista.append(num)
        except ValueError:
            print("Error: debe ingresar un numero entero.")
    return lista


def buscar_elemento(lista: list[int]) -> None:
    """
    Permite buscar numeros dentro de una lista e informa su posicion usando index().
    Aborta el proceso luego de 3 errores consecutivos.

    Precondicion:
    La lista debe contener al menos un elemento.
    Poscondicion:
    Muestra por pantalla la posición del numero buscado o un mensaje de error.
    """
    errores = 0
    while errores < 3:
        try:
            valor = int(input("\nIngrese el numero que desea buscar: "))
            posicion = lista.index(valor)
            print(f"El numero {valor} se encuentra en la posición {posicion}.")
        except ValueError:
            errores += 1
            print(f"Error: el numero no está en la lista. ({errores} errores)")
        except Exception:
            errores += 1
            print(f"Error desconocido. ({errores} errores)")
    print("\nSe alcanzó el maximo de errores. Busqueda finalizada.")


def main() -> None:
    """
    Ejecuta el programa de carga y busqueda de elementos en una lista.

    Precondicion:
    Ninguna.
    Poscondicion:
    El usuario puede buscar elementos hasta cometer tres errores.
    """
    lista = cargar_lista()
    if lista:
        buscar_elemento(lista)
    else:
        print("No se ingresaron datos.")


if __name__ == "__main__":
    main()
