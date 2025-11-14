# TP 6 Ejercicio 1
import os
print("Ruta actual:", os.getcwd())

def clasificar_nombres():
    '''Clasifica los apellidos de un documento txt entre armenia, italia y españa en funcion
    de la terminacion del apellido.
    Precondiciones: recibe un archivo txt con apellido,nombre
    Poscondiciones: Guarda los archivos por separado segun el pais.'''
    ruta = r"C:\Users\Vaio\Documents\TPS de AyED\TP6\nombres.txt"
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue

                apellido = linea.split(",")[0].strip().lower()

                if apellido.endswith("ian"):
                    destino = r"C:\Users\Vaio\Documents\TPS de AyED\TP6\ARMENIA.TXT"
                elif apellido.endswith("ini"):
                    destino = r"C:\Users\Vaio\Documents\TPS de AyED\TP6\ITALIA.TXT"
                elif apellido.endswith("ez"):
                    destino = r"C:\Users\Vaio\Documents\TPS de AyED\TP6\ESPAÑA.TXT"
                else:
                    continue

                with open(destino, "a", encoding="utf-8") as salida:
                    salida.write(linea + "\n")

        print("Archivos generados correctamente.")

    except FileNotFoundError:
        print("ERROR: No se encontró el archivo nombres.txt")

clasificar_nombres()
