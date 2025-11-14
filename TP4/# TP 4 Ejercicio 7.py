# TP 4 Ejercicio 7
def eliminar_subcadena_rebanadas(cadena, posicion, cantidad):
    return cadena[:posicion] + cadena[posicion + cantidad:]

if __name__ == "__main__":
    texto = "El numero de teléfono es 4356-7890"
    resultado = eliminar_subcadena_rebanadas(texto, 25, 9)
    print("Original:", texto)
    print("Modificada:", resultado)


def eliminar_subcadena_sin_rebanadas(cadena, posicion, cantidad):
    nueva_cadena = ""
    for i in range(len(cadena)):
        if not (posicion <= i < posicion + cantidad):
            nueva_cadena += cadena[i]
    return nueva_cadena

if __name__ == "__main__":
    texto = "El numero de teléfono es 4356-7890"
    resultado = eliminar_subcadena_sin_rebanadas(texto, 25, 9)
    print("Original:", texto)
    print("Modificada:", resultado)
