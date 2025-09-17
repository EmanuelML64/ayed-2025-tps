# TP 1 Ejercicio 9
# Algoritmos y estructuras de datos
import random
def cosecha(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(150,350))
    return lista
def cajones(lis):
    cajones = []
    cantidad = 0
    peso = 0
    for naranja in lis:
        if naranja >= 200 and naranja <= 300:
            peso += naranja
            cantidad += 1
        if cantidad == 100:
            cajones.append(peso)
            cantidad = 0
            peso = 0
    if cantidad:
        cajones.append(peso)
    sobrante = cantidad
    return cajones, len(cajones), sobrante

def jugo(lis):
    total = 0
    for naranja in lis:
        if naranja < 200 or naranja > 300:
            total += 1
    return total

def camiones(camion,cajones):
    cajonesllenos = []
    peso = 0
    for cajon in cajones:
        peso += cajon
        if peso > camion:
            cajonesllenos.append((peso-cajon)/1000)
            peso = cajon
        return cajonesllenos,peso
    
if __name__ == "__main__":
    cantidadxcajon = 100
    cantidaddecamiones = 35
    capacidaddelcamion = 100000
    cantidadnaranjas = 20000

    cosechadas = cosecha(cantidadnaranjas)
    pesodecajones,cantidaddecajones,sobraron = cajones(cosechadas)
    pesototal = sum(cosechadas)

    print(f"Se cosecharon{pesototal/1000000:.3f} Toneladas de naranjas")
    print(f"Hay {jugo(cosechadas)} naranjas para jugo de un total de {cantidadnaranjas} ")
    print(f"Hay {cantidaddecajones} cajones para cargar")
    print(f"Y sobraron {sobraron} naranjas que no completaron el ultimo cajon")

    camioncargado,ultimo = camiones(capacidaddelcamion,pesodecajones)
    for i,peso in enumerate(camioncargado):
        if i < cantidaddecamiones:
            print(f"En el camion{i+1:>2} van {peso} kilos")
        
    if len(camioncargado) > cantidaddecamiones:
        print(f"Hay carga para despachar {len(camioncargado) - cantidaddecamiones} camiones mas")
    else:
        print(f"Hay carga para despachar {len(camioncargado)} camiones llenos")