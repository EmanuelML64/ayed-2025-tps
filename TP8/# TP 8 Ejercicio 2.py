# TP 8 Ejercicio 2


MESES = (
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
)

ANIO_CORTE = 30   # Todo año 2 dígitos > 30 es del siglo pasado (1900)


def fecha_extendida(fecha: tuple[int, int, int]) -> str:
    """
    Convierte una tupla (día, mes, año) a una fecha en formato extendido.

    Reglas:
    - Si el año tiene 4 dígitos, se usa tal cual.
    - Si tiene 2 dígitos:
        * Año <= ANIO_CORTE → interpretado como 2000–2030
        * Año > ANIO_CORTE → interpretado como 1900–1999

    Args:
        fecha (tuple[int, int, int]): (día, mes, año)

    Returns:
        str: Fecha en formato "D de <Mes> de AAAA".
    """
    dia, mes, anio = fecha

    # Interpretación del año
    if 0 <= anio <= 99:  # Año de dos dígitos
        if anio <= ANIO_CORTE:
            anio = 2000 + anio
        else:
            anio = 1900 + anio

    # Obtener nombre del mes
    nombre_mes = MESES[mes - 1]

    return f"{dia} de {nombre_mes} de {anio}"


def main() -> None:
    """
    Programa principal:
    - Pide fecha al usuario
    - Convierte a formato extendido
    - Muestra resultado
    """
    print("Ingrese una fecha:")

    try:
        d = int(input("Día: "))
        m = int(input("Mes: "))
        a = int(input("Año (2 o 4 dígitos): "))
    except ValueError:
        print("Error: Debe ingresar números enteros.")
        return

    resultado = fecha_extendida((d, m, a))
    print("\nFecha en formato extendido:")
    print(resultado)


if __name__ == "__main__":
    main()
