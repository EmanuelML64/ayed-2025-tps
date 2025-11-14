# TP 8 Ejercicio 1

def es_bisiesto(anio: int) -> bool:
    """
    Determina si un año es bisiesto.

    Precondiciones:
    anio (int): Año a verificar.

    Poscondiciones:
    bool: True si es bisiesto, False en caso contrario.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def dias_en_mes(mes: int, anio: int) -> int:
    """
    Devuelve la cantidad de días que tiene un mes determinado.

    Precondiciones:
    mes (int): Mes (1-12).
    anio (int): Año asociado.

    Poscondiciones:
    int: Cantidad de días del mes.
    """
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if mes in (4, 6, 9, 11):
        return 30
    if mes == 2:
        return 29 if es_bisiesto(anio) else 28
    return 0


def ingresar_fecha() -> tuple[int, int, int]:
    """
    Solicita una fecha válida por teclado.

    Poscondiciones:
    tuple[int, int, int]: Fecha como (día, mes, año).
    """
    while True:
        try:
            dia = int(input("Día: "))
            mes = int(input("Mes: "))
            anio = int(input("Año: "))

            if 1 <= mes <= 12 and 1 <= dia <= dias_en_mes(mes, anio):
                return (dia, mes, anio)
            else:
                print("Fecha inválida. Intente nuevamente.\n")
        except ValueError:
            print("Error: debe ingresar números.\n")


def sumar_dias(fecha: tuple[int, int, int], n: int) -> tuple[int, int, int]:
    """
    Suma N días a una fecha sin usar librerías.

    Precondiciones:
    fecha (tuple[int,int,int]): Fecha original (d, m, a).
    n (int): Cantidad de días a sumar.

    Poscondiciones:
    tuple[int,int,int]: Nueva fecha resultante.
    """
    dia, mes, anio = fecha

    for _ in range(n):
        dia += 1
        if dia > dias_en_mes(mes, anio):
            dia = 1
            mes += 1
            if mes > 12:
                mes = 1
                anio += 1

    return (dia, mes, anio)




def ingresar_horario() -> tuple[int, int, int]:
    """
    Solicita un horario válido por teclado.

    Poscondiciones:
    tuple[int,int,int]: Horario como (hora, minuto, segundo).
    """
    while True:
        try:
            h = int(input("Hora (0-23): "))
            m = int(input("Minuto (0-59): "))
            s = int(input("Segundo (0-59): "))

            if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
                return (h, m, s)
            else:
                print("Horario inválido.\n")
        except ValueError:
            print("Error: debe ingresar números válidos.\n")


def a_segundos(horario: tuple[int, int, int]) -> int:
    """
    Convierte un horario a segundos.

    Precondiciones:
    horario (tuple[int,int,int]): (h, m, s).

    Poscondiciones:
    int: Total de segundos.
    """
    h, m, s = horario
    return h * 3600 + m * 60 + s


def diferencia_horarios(h1: tuple[int, int, int],
                        h2: tuple[int, int, int]) -> tuple[int, int, int]:
    """
    Calcula la diferencia entre dos horarios.

    Si el primer horario es mayor que el segundo,
    se considera que pertenece al día anterior.

    La diferencia nunca puede superar 24 horas.

    Precondiciones:
        h1 (tuple[int,int,int]): Horario inicial.
        h2 (tuple[int,int,int]): Horario final.

    Poscondiciones:
        tuple[int,int,int]: Diferencia (horas, minutos, segundos).
    """
    t1 = a_segundos(h1)
    t2 = a_segundos(h2)

    if t1 > t2:
        t2 += 24 * 3600  # h1 fue el día anterior

    dif = t2 - t1

    if dif > 24 * 3600:
        dif = 24 * 3600

    horas = dif // 3600
    minutos = (dif % 3600) // 60
    segundos = dif % 60

    return (horas, minutos, segundos)



def main() -> None:
    """
    Demostracion de todas las funciones solicitadas.
    """
    print("\n--- Ingreso de fecha valida ---")
    fecha = ingresar_fecha()
    print("Fecha ingresada:", fecha)

    print("\n--- Sumar dias ---")
    n = int(input("Cuantos dias desea sumar: "))
    nueva_fecha = sumar_dias(fecha, n)
    print("Resultado:", nueva_fecha)

    print("\n--- Ingreso de horarios ---")
    print("Horario 1:")
    h1 = ingresar_horario()
    print("Horario 2:")
    h2 = ingresar_horario()

    print("\n--- Diferencia entre horarios ---")
    dif = diferencia_horarios(h1, h2)
    print("La diferencia es:", dif, " (h, m, s)")



if __name__ == "__main__":
    main()
