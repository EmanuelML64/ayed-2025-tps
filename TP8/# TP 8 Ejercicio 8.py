# TP 8 Ejercicio 8
def generar_diccionario_cuadrados() -> dict[int, int]:
    """
    Genera un diccionario cuyas claves son los números del 1 al 20
    y los valores son el cuadrado de esas claves.
    """
    return {n: n * n for n in range(1, 21)}

def main():
    dic = generar_diccionario_cuadrados()
    print(dic)

if __name__ == "__main__":
    main()
