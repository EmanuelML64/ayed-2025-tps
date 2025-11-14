# TP Ejercicio 3
def GrabarRangoAlturas():
    with open("alturas.txt", "w", encoding="utf-8") as archivo:
        while True:
            deporte = input("Ingrese nombre del deporte (o FIN para terminar): ")
            if deporte.upper() == "FIN":
                break

            archivo.write(deporte + "\n")

            print(f"Ingrese alturas para {deporte} (ENTER sin valor para finalizar).")
            while True:
                altura = input("Altura: ")
                if altura == "":
                    break
                archivo.write(altura + "\n")


def GrabarPromedio():
    try:
        with open("alturas.txt", "r", encoding="utf-8") as archivo_alturas, \
             open("promedios.txt", "w", encoding="utf-8") as archivo_prom:

            linea = archivo_alturas.readline()
            while linea != "":
                deporte = linea.strip()
                alturas = []

                linea = archivo_alturas.readline()
                while linea != "" and linea.strip().isdigit():
                    alturas.append(int(linea.strip()))
                    linea = archivo_alturas.readline()

                if len(alturas) > 0:
                    promedio = sum(alturas) / len(alturas)
                    archivo_prom.write(f"{deporte}\n{promedio:.2f}\n")

    except FileNotFoundError:
        print("ERROR: No existe el archivo alturas.txt")


def MostrarMasAltos():
    try:
        deportes = []
        promedios = []

        with open("promedios.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for i in range(0, len(lineas), 2):
                deporte = lineas[i].strip()
                promedio = float(lineas[i+1].strip())

                deportes.append(deporte)
                promedios.append(promedio)

        if len(promedios) == 0:
            print("No hay datos para analizar.")
            return

        promedio_general = sum(promedios) / len(promedios)
        print(f"Promedio general de alturas: {promedio_general:.2f} cm\n")
        print("Deportes con promedio superior:")

        for deporte, prom in zip(deportes, promedios):
            if prom > promedio_general:
                print(f"- {deporte} ({prom:.2f} cm)")

    except FileNotFoundError:
        print("ERROR: No existe el archivo promedios.txt")
