# TP 8 Ejercicio 3
from typing import Tuple


def descomponer_correo(correo: str) -> Tuple[str, ...]:
    """
    Descompone una dirección de correo electrónico en sus partes.

    Parámetros
    
    correo : str
        Cadena que contiene una dirección de correo electrónico.

    Retorna
    
    Tuple[str, ...]
        Una tupla con las partes que componen el correo.
        Ejemplo:
            "alguien@uade.edu.ar" -> ("alguien", "uade", "edu", "ar")

        Si el formato es inválido, retorna una tupla vacía.
    """

    if correo.count('@') != 1:
        return ()

    usuario, dominio = correo.split('@')


    if not usuario or ' ' in usuario:
        return ()


    partes_dominio = dominio.split('.')

    if len(partes_dominio) < 2:
        return ()


    for parte in partes_dominio:
        if not parte or ' ' in parte:
            return ()

    return (usuario, *partes_dominio)




print(descomponer_correo("alguien@uade.edu.ar"))   
print(descomponer_correo("correo@dominio"))         
print(descomponer_correo("sin_arroba.com"))         
print(descomponer_correo("invalido@dominio."))      
