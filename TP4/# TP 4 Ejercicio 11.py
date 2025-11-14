# TP 4 Ejercicio 11
def contar_subcadena(cadena: str, subcadena: str) -> int:
    '''
    Cuenta cuantas veces aparece una subcadena dentro de una cadena,
    sin diferenciar mayusculas y minusculas. Los caracteres de la
    subcadena no necesariamente deben ser consecutivos, pero sí deben
    respetar el orden.

    Precondiciones:
    cadena y subcadena son cadenas de caracteres no vacias.
    

    Poscondiciones:
    Devuelve un numero entero ≥ 0 que representa la cantidad de
      veces que la subcadena puede encontrarse respetando el orden.
    '''

    cadena = cadena.lower()
    subcadena = subcadena.lower()

    i = 0  
    contador = 0

    for caracter in cadena:
        if caracter == subcadena[i]:
            i += 1
            if i == len(subcadena):
                contador += 1
                i = 0  

    return contador



if __name__ == "__main__":
    texto: str = ("Platero es pequeño, peludo, suave; tan blando por fuera, "
                  "que se diría todo de algodón, que no lleva huesos. "
                  "Sólo los espejos de azabache de sus ojos son duros cual "
                  "dos escarabajos de cristal negro.")
    sub: str = "UADE"

    cantidad: int = contar_subcadena(texto, sub)

    print("Cadena:", texto)
    print("Subcadena:", sub)
    print("Cantidad encontrada:", cantidad)
