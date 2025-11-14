# TP 8 Ejercicio 9
def generar_tabla(n: int) -> dict[int, int]:
    """
    Genera un diccionario con la tabla de multiplicar de n del 1 al 12.
    """
    return {i: n * i for i in range(1, 13)}

def main():
    n = int(input("Ingrese un numero entero: "))
    tabla = generar_tabla(n)

    print(f"\nTABLA DE MULTIPLICAR DEL {n}\n")
    for i, resultado in tabla.items():
        print(f"{n} x {i:2} = {resultado}")

if __name__ == "__main__":
    main()
