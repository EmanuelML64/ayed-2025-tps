# TP 4 Ejercicio 8
def ultimos_n_caracteres(cadena, n):
    return cadena[-n:]  

if __name__ == "__main__":
    texto = "Morocha hermosa"
    resultado = ultimos_n_caracteres(texto, 7)
    print("Original:", texto)
    print("Últimos 7 caracteres:", resultado)
