# TP 4 Ejercicio 14
def validar_email(email: str) -> bool:
    """
    Verifica si una dirección de correo electrónico es valida segun las siguientes reglas:
    Solo un '@' en toda la cadena.
    El nombre de usuario solo puede contener caracteres alfanumericos.
    El dominio debe tener al menos un caracter y terminar en '.com' o '.com.ar'.

    Precondicion:
    email es una cadena de texto no vacia que representa una dirección de correo a validar.
    Poscondicion:
    Devuelve True si el correo cumple con todos los criterios de validez; False en caso contrario.
    """
    email = email.lower().strip()

    if email.count("@") != 1:
        return False

    usuario, dominio = email.split("@")

    if not usuario.isalnum():
        return False

    if not (dominio.endswith(".com") or dominio.endswith(".com.ar")):
        return False

    if len(dominio.split(".")[0]) == 0:  # dominio vacío antes del primer punto
        return False

    return True


def main() -> None:
    """
    Lee direcciones de correo electrónico hasta ingresar una cadena vacía, valida cada una
    e imprime al final los dominios válidos sin repetir y ordenados alfabéticamente.

    Precondición:
    El usuario debe ingresar direcciones de correo válidas o vacías para finalizar.
    Poscondición:
    Muestra una lista alfabética de dominios válidos únicos.
    """
    dominios: set[str] = set()

    while True:
        email = input("Ingrese una dirección de correo (vacío para terminar): ").strip()
        if email == "":
            break

        if validar_email(email):
            dominio = email.lower().split("@")[1]
            dominios.add(dominio)
            print(" Dirección válida.")
        else:
            print(" Dirección inválida.")

    print("\nDominios válidos :")
    for d in sorted(dominios):
        print("-", d)


if __name__ == "__main__":
    main()
