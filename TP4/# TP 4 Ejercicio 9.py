# TP 4 Ejercicio 9
def ordenar_por_longitud(frase: str) -> str:
    '''Ordena la cadena en funcion de su longitud.
    Precondiciones: cadena de caracteres separada por espacios.
    Poscondiciones: cadena con palabras ordenadas por longitud'''
    palabras = frase.split()
    
    
    signos = ".,;:!?¡¿()[]{}\"'"
    
    
    def longitud_real(palabra: str) -> int:
        limpia = ""
        for c in palabra:
            if c not in signos:
                limpia += c
        return len(limpia)
    
    
    palabras_ordenadas = sorted(palabras, key=longitud_real)
    
    
    return " ".join(palabras_ordenadas)



if __name__ == "__main__":
    texto = "Hola,   mi amorr!!! esto es  un  ejemplo."
    resultado = ordenar_por_longitud(texto)
    print("Original:", texto)
    print("Ordenada:", resultado)
