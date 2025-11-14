# TP 4 Ejercicio 10
def reemplazar_palabra(texto: str, palabra_original: str, nueva_palabra: str) -> tuple:
    '''Reemplaza todas las apariciones de una palabra por otra.
    Precondiciones: cadena de caracteres y palabra que lo reemplazara.
    Poscondiciones: cadena obtenida y reemplazos realizados'''
    palabras = texto.split()
    reemplazos = 0
    resultado = []

    for palabra in palabras:
        prefijo = ""
        sufijo = ""
        while len(palabra) > 0 and not palabra[0].isalnum():
            prefijo += palabra[0]
            palabra = palabra[1:]
        while len(palabra) > 0 and not palabra[-1].isalnum():
            sufijo = palabra[-1] + sufijo
            palabra = palabra[:-1]

        
        if palabra == palabra_original:
            palabra = nueva_palabra
            reemplazos += 1

        
        resultado.append(prefijo + palabra + sufijo)

    return " ".join(resultado), reemplazos



if __name__ == "__main__":
    texto = "Hola hermano, un abrazo!"
    nueva_cadena, cantidad = reemplazar_palabra(texto, "hermano", "abrazo")

    print("Texto original:", texto)
    print("Texto modificado:", nueva_cadena)
    print("Reemplazos realizados:", cantidad)
