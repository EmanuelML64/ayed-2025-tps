# TP 8 Ejercicio 10 
def eliminar_claves(dic: dict, claves: list) -> tuple[dict, int]:
    """
    Elimina del diccionario 'dic' todas las claves presentes en la lista 'claves'.
    Devuelve una tupla con:
    el diccionario modificado
    la cantidad de claves eliminadas
    """
    eliminadas = 0

    for clave in claves:
        if clave in dic:
            del dic[clave]
            eliminadas += 1

    return dic, eliminadas


def main():
    
    datos = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }

    print("Diccionario original:", datos)

    
    claves_a_eliminar = ["b", "d", "x"]  

    dic_modificado, cantidad = eliminar_claves(datos, claves_a_eliminar)

    print("\nDiccionario modificado:", dic_modificado)
    print("Cantidad de claves eliminadas:", cantidad)


if __name__ == "__main__":
    main()
