# TP 4 Ejercicio 13
def numero_a_letras(n: int) -> str:
    '''
    Convierte un número entero entre 0 y 1 billon (1.000.000.000.000) a su forma escrita en español.

    Precondicion: n es un numero entero no negativo menor o igual a 1 billon.
    Poscondicion: devuelve una cadena con el número expresado en letras.
    '''

    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince",
                  "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta",
               "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos",
                "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    if n == 0:
        return "cero"
    if n == 100:
        return "cien"
    if n == 1_000_000_000_000:
        return "un billón"

    def tres_cifras(num: int) -> str:
        """
    Convierte un numero entero entre 0 y 999 en su representación escrita en letras en español.

    Precondición:
        El numero num debe ser un entero comprendido entre 0 y 999 inclusive.

    Poscondición:
        Devuelve una cadena con la representacion textual correcta del numero en español, 
        sin espacios innecesarios y con las palabras separadas por un solo espacio.
    """
        c, r = divmod(num, 100)
        d, u = divmod(r, 10)
        if r == 0:
            return centenas[c]
        if r < 10:
            return (centenas[c] + " " + unidades[u]).strip()
        if 10 <= r < 20:
            return (centenas[c] + " " + especiales[r - 10]).strip()
        if d == 2 and u != 0:
            return (centenas[c] + " veinti" + unidades[u]).strip()
        if u == 0:
            return (centenas[c] + " " + decenas[d]).strip()
        return (centenas[c] + " " + decenas[d] + " y " + unidades[u]).strip()

    partes = [
        (1_000_000_000, "mil millones"),
        (1_000_000, "millon", "millones"),
        (1_000, "mil")
    ]

    resultado = ""
    for valor, *nombres in partes:
        cantidad, n = divmod(n, valor)
        if cantidad:
            nombre = nombres[0] if len(nombres) == 1 else (nombres[0] if cantidad == 1 else nombres[1])
            resultado += tres_cifras(cantidad) + " " + nombre + " "
        n = n

    resultado += tres_cifras(n)
    return resultado.strip()



if __name__ == "__main__":
    numero: int = int(input("Ingrese un numero entre 0 y 1 billon: "))
    print(numero_a_letras(numero))
