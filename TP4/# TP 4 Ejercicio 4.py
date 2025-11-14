# TP 4 Ejercicio 4
def entero_a_romano(num: int) -> str:
    """
    Convierte un número entero (0-3999) en su representación romana.
    Precondición: 0 <= num <= 3999.
    Poscondición: Retorna una cadena con el número en formato romano.
    """
    if not (0 <= num <= 3999):
        raise ValueError("El número debe estar entre 0 y 3999.")

    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    romano = ""
    for valor, simbolo in valores:
        while num >= valor:
            romano += simbolo
            num -= valor
    return romano

print(entero_a_romano(3999))
print(entero_a_romano(5))
print(entero_a_romano(14))