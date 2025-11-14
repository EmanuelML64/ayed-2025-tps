# TP 4 Ejercicio 6
def subcadena_rebanada(cadena: str, inicio: int, cantidad: int) -> str:
    """
    Devuelve una subcadena utilizando rebanadas.
    Precondición: 0 <= inicio < len(cadena), cantidad >= 0
    Poscondición: Retorna una cadena con los caracteres que queress.
    """
    return cadena[inicio:inicio + cantidad]

def subcadena_manual(cadena: str, inicio: int, cantidad: int) -> str:
    """
    Devuelve una subcadena sin usar rebanadas.
    Precondición: 0 <= inicio < len(cadena), cantidad >= 0
    Poscondición: Retorna una cadena con los caracteres que queres.
    """
    resultado = ""
    fin = inicio + cantidad
    for i in range(inicio, min(fin, len(cadena))):
        resultado += cadena[i]
    return resultado


cadena = "El número de teléfono es 4356-7890"
inicio = 25
cantidad = 9

print("Cadena original:", cadena)
print("Subcadena (rebanadas):", subcadena_rebanada(cadena, inicio, cantidad))
print("Subcadena (manual):   ", subcadena_manual(cadena, inicio, cantidad))