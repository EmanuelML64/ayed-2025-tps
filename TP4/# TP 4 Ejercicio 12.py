# TP 4 Ejercicio 12
def crear_baraja() -> list[str]:
    '''
    Crea una lista con todos los naipes de la baraja española.

    Precondiciones:
    No recibe parametros.La baraja española se compone de 4 palos: "Oros", "Copas", "Espadas" y "Bastos".
    Cada palo tiene las cartas del 1 al 12.

    Poscondiciones:
    Devuelve una lista de cadenas de caracteres con los 48 naipes,
    en formato "numero palo".
    '''
    palos: list[str] = ["Oros", "Copas", "Espadas", "Bastos"]
    baraja: list[str] = [f"{numero} {palo}" for palo in palos for numero in range(1, 13)]
    return baraja



if __name__ == "__main__":
    naipes: list[str] = crear_baraja()
    print("Baraja española:")
    print(naipes)
