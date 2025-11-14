# TP 4 Ejercicio 1
def es_capicua(cadena:str)->bool:
    '''Recibe una cadena de caracteres y comprueba si es igual del derecho o del reves.
    Precondiciones: recibe una cadena de caracteres.
    Poscondiciones: devuelve True si es capicua y False si no lo es.'''
    inicio = 0
    fin = len(cadena) - 1
    while inicio < fin:
        if cadena[inicio] != cadena[fin]:
            return False
        inicio += 1
        fin -= 1
    return True


texto = input("Ingrese una cadena: ")

if es_capicua(texto):
    print("La cadena es capicúa.")
else:
    print("La cadena no es capicúa.")

