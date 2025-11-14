# TP 6 Ejercicio 6
import os
import random as rn
from datetime import datetime
from tabulate import tabulate

ARCHIVO = "huespedes.csv"



def registrar_huespedes():
    print("=== REGISTRO DE HUÉSPEDES ===")

    if not os.path.exists(ARCHIVO):
        open(ARCHIVO, "w").close()

    dnis = set()


    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) > 0:
                dnis.add(int(partes[0]))

    while True:
        dni = int(input("DNI del huesped (-1 para finalizar): "))
        if dni == -1:
            break

        if dni in dnis:
            print(" Este DNI ya está registrado.")
            continue

        nombre = input("Apellido y Nombre: ")

        ingreso = input("Fecha ingreso (DDMMAAAA): ")
        egreso = input("Fecha egreso (DDMMAAAA): ")

        if int(egreso) <= int(ingreso):
            print("ERROR: la fecha de egreso debe ser mayor a la de ingreso.")
            continue

        ocupantes = int(input("Cantidad de ocupantes: "))

        # Guardamos como CSV común (sin librería csv)
        with open(ARCHIVO, "a", encoding="utf-8") as f:
            f.write(f"{dni},{nombre},{ingreso},{egreso},{ocupantes}\n")

        dnis.add(dni)
        print(" Registrado correctamente.\n")




def leer_huespedes():
    huespedes = []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            dni, nombre, ing, egr, ocup = linea.strip().split(",")
            huespedes.append({
                "dni": int(dni),
                "nombre": nombre,
                "ingreso": ing,
                "egreso": egr,
                "ocupantes": int(ocup)
            })
    return huespedes


def asignar_habitaciones(huespedes):
    habitaciones_ocupadas = {}  
    disponibles = [(p, h) for p in range(1, 11) for h in range(1, 7)]

    for h in huespedes:
        hab = rn.choice(disponibles)
        disponibles.remove(hab)

        h["piso"] = hab[0]
        h["hab"] = hab[1]

        habitaciones_ocupadas[hab] = h

    return habitaciones_ocupadas, disponibles



def piso_con_mas_ocupadas(habs):
    contador = [0] * 11  
    for (p, h) in habs:
        contador[p] += 1
    return contador.index(max(contador[1:]))

def habitaciones_vacias(disponibles):
    return len(disponibles)

def piso_con_mas_personas(habs):
    personas = [0] * 11
    for (p, h), huésped in habs.items():
        personas[p] += huésped["ocupantes"]
    return personas.index(max(personas[1:]))

def proxima_en_desocuparse(habs, fecha_actual):
    fecha_actual = int(fecha_actual)
    min_fecha = min(int(h["egreso"]) for h in habs.values())

    return [
        (p, h, datos)
        for (p, h), datos in habs.items()
        if int(datos["egreso"]) == min_fecha
    ]

def listado_ordenado(habs):
    lista = []
    for (p, h), hu in habs.items():
        dias = (datetime.strptime(hu["egreso"], "%d%m%Y") -
                datetime.strptime(hu["ingreso"], "%d%m%Y")).days
        lista.append([hu["nombre"], hu["dni"], p, h, dias])

    lista.sort(key=lambda x: x[4])  

    print("\n=== LISTADO ORDENADO POR DIAS ===")
    print(tabulate(lista, headers=["Nombre", "DNI", "Piso", "Hab", "Dias"]))



def main():
    registrar_huespedes()

    huespedes = leer_huespedes()
    habs, disponibles = asignar_habitaciones(huespedes)

    print("\n=== RESULTADOS ===")

    print(f"a) Piso con mas ocupadas: {piso_con_mas_ocupadas(habs)}")
    print(f"b) Habitaciones vacías: {habitaciones_vacias(disponibles)}")
    print(f"c) Piso con más personas: {piso_con_mas_personas(habs)}")

    fecha_act = input("Ingrese fecha actual (DDMMAAAA): ")
    prox = proxima_en_desocuparse(habs, fecha_act)

    print("\nd) Proxima habitación en desocuparse:")
    for p, h, dat in prox:
        print(f"Piso {p}, Hab {h}, Huesped: {dat['nombre']}")

    listado_ordenado(habs)


main()
