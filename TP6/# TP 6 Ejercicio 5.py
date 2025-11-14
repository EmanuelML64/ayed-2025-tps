# TP 6 Ejercicio 5
def convertir_formato1(origen, destino):
    try:
        with open(origen, "r", encoding="utf-8") as f_in, \
             open(destino, "w", encoding="utf-8") as f_out:

            for linea in f_in:
                apellido_nombre = linea[0:12].rstrip()
                fecha_alta = linea[12:20].rstrip()
                domicilio = linea[21:].rstrip()

                f_out.write(f"{apellido_nombre},{fecha_alta},{domicilio}\n")

        print("Conversion FORMATO 1 → CSV completa.")

    except FileNotFoundError:
        print("ERROR: no se encontro el archivo.")


def convertir_formato2(origen, destino):
    try:
        with open(origen, "r", encoding="utf-8") as f_in, \
             open(destino, "w", encoding="utf-8") as f_out:

            for linea in f_in:
                campos = []
                i = 0

                while i < len(linea):
                    largo = int(linea[i:i+2])
                    i += 2
                    campo = linea[i:i+largo]
                    campos.append(campo)
                    i += largo

                
                f_out.write(",".join(campos) + "\n")

        print("Conversion FORMATO 2 → CSV completa.")

    except FileNotFoundError:
        print("ERROR: no se encontro el archivo.")



if __name__ == "__main__":

    print("1 = Formato 1    |    2 = Formato 2")
    opcion = input("¿Qué archivo queres convertir? ")

    origen = input("Nombre del archivo de entrada: ")
    destino = input("Nombre del archivo CSV de salida: ")

    if opcion == "1":
        convertir_formato1(origen, destino)
    elif opcion == "2":
        convertir_formato2(origen, destino)
    else:
        print("Opcion no valida.")
