# TP 6 Ejercicio 2
def dividir_archivo(nombre_archivo: str, tamaño_maximo: int) -> None:
    """
    Precondiciones: nombre_archivo debe existir y tamaño_maximo debe ser un entero mayor que 0.
    Poscondiciones: crea archivos del tipo nombre_archivo_parteX.txt sin cortar líneas, 
    o muestra un mensaje de error si no puede realizarse.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            parte = 1
            tamaño_actual = 0
            archivo_salida = open(f"{nombre_archivo}_parte{parte}.txt",
                                  "w", encoding="utf-8")

            for linea in archivo:
                tamaño_linea = len(linea.encode("utf-8"))  

                
                if tamaño_linea > tamaño_maximo:
                    print(f"Error: una línea supera los {tamaño_maximo} bytes.")
                    archivo_salida.close()
                    return

                
                if tamaño_actual + tamaño_linea > tamaño_maximo:
                    archivo_salida.close()
                    parte += 1
                    tamaño_actual = 0
                    archivo_salida = open(f"{nombre_archivo}_parte{parte}.txt",
                                          "w", encoding="utf-8")

                archivo_salida.write(linea)
                tamaño_actual += tamaño_linea

            archivo_salida.close()
            print(f"Archivo dividido en {parte} parte(s).")

    except FileNotFoundError:
        print("Error: No se encontró el archivo.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def main() -> None:
    nombre = input("Ingrese el nombre del archivo a dividir: ")
    try:
        tamaño = int(input("Ingrese el tamaño máximo por parte (en bytes): "))
        dividir_archivo(nombre, tamaño)
    except ValueError:
        print("Error: Debe ingresar un número entero.")


if __name__ == "__main__":
    main()
