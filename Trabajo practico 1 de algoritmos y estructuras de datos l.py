# Ejercicios AyED
# 1 
def mayor(num1,num2,num3):
    numeros = [num1,num2,num3]
    maximo = max(numeros)
    
    apariciones = 0
    if maximo == num1:
        apariciones += 1
    if maximo == num2:
        apariciones += 1
    if maximo == num3:
        apariciones += 1

    if apariciones == 1:
        return maximo
    else:
        return -1
    
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese otro numero: "))

resultado = mayor(num1,num2,num3)
if resultado == -1:
    print("No hay un mayor estricto")
else:
    print("El mayor es: ", resultado)

# 2
def fecha(d,m,a):
    valido = True
    if d > 31:
        valido = False
    if m == 2 and d >= 30:
        valido = False
    if m < 1 or m > 12:
        valido = False
    if a > 2025:
        valido = False
    return valido
dia = int(input("Ingrese un dia: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))
comprobacion = fecha(dia,mes,anio)
print(comprobacion)
    


# 3
def tarifasubte(viajes):
    tarifa = 1000
    masde20 = 800
    masde30 = 700
    masde40 = 600
    if viajes <= 20:
        costo = viajes*tarifa
    elif viajes > 20 and viajes <= 30:
        costo = (viajes - 20) * masde20 + 20 * tarifa
    elif viajes > 30 and viajes <= 40:
        costo = (viajes - 30) * masde30 + 10 * masde20 + 20 * tarifa
    else:
        costo = (viajes - 40) * masde40 + 10 * masde30 + 10 * masde20 + 20 * tarifa
    return costo
cantidad = int(input("Ingrese la cantidad de viajes realizados: "))
total = tarifasubte(cantidad)
print("Su costo es ", total, "$")


# 4
def vuelto(total: int, recibido: int) -> list:
    if total > recibido:
        return [-1]
    # Crea una lista de 7 elementos en cero
    billetes = []
    # Calculo lo que debe devolver
    devolver = recibido - total
    for v in valores:
        billetes.append(devolver//v)
        devolver %= v     # Guardo el resto de la division
    return billetes

valores = [500,100,50,20,10,5,2,1]
pago = 496
billete = 1000
if pago > billete:
    print("No alcanza para hacer el pago")
else:
    salida = vuelto(pago,billete)
    # Uso de enumerate para las listas
    for i,s in enumerate(salida): # Ver enumerate
        if s:    # Revisa si es verdadero o falso, tomando 1 como True y 0 como False. Es lo mismo que s != 0
            print(f"{s} billetes de {valores[i]}")
# Enumerate devuelve una tupla con (indice,valor), elemento inmutable e iterable
# El desempaquetado de datos seria asi: indice,dato = (0,500)
# print(indice): 0
# print(dato): 500
# Tambien se puede usar divmod(a,b), devolviendo una tupla (a//b),(a%b)

# 5
es_oblongo = lambda n: any(i * (i + 1) == n for i in range(1, n))
print(es_oblongo(6))
print(es_oblongo(5))


es_triangular = lambda n: any(i*(i+1)//2 == n for i in range(1, n+1))
print(es_triangular(10))
print(es_triangular(9))



# 6
def conca(x,y):
    return str(x) + str(y)

num1 = int(input("Ingrese un numero para concatenar: "))
num2 = int(input("Ingrese otro numero para concatenar: "))
resultado = conca(num1,num2)
print(resultado)

# 7
def diasiguiente(dia,mes,anio):
    if dia == 31 and mes == 12:
        diasig = 1
        messig = 1
        aniosig = anio + 1
    elif dia == 31 and mes > 0 and mes < 12:
        diasig = 1
        messig = mes + 1
        aniosig = anio
    else:
        diasig = dia + 1
        messig = mes
        aniosig = anio
    return diasig,messig,aniosig

day = int(input("Ingrese el dia a comprobar: "))
month = int(input("Ingrese el mes a comprobar: "))
year = int(input("Ingrese el año a comprobar: "))
sigday = diasiguiente(day,month,year)
print(sigday)

# Sumar N dias
n = int(input("Ingrese la cantidad de dias a sumar: "))
for i in range(n):
    day,month,year = diasiguiente(day,month,year)
print(day,month,year)

# 8 
def diadelasemana(dia,mes,anio):
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    siglo = anio//10044444444
    anio2 = anio%100
    diasem = (((26*mes - 2)//10)+dia+anio2+(anio2//4) + (siglo//4) - (2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def elmes(dia,dias):
    listames = []
    if dia:
        for i in range(dia):
            listames.append(0)
    for day in range(1,dias+1):
        listames.append(day)
    
    return listames

def calendario(mes,dia,anio):
    print(f"{meses[dia - 1]} de {anio}")
    for day in semana:    # DONDE ESTA DECLARADO SEMANA ? 
        print(f"{day}", end = " ")
    print(f"{"-"*len(semana)*4}")
    contador = 0
    for day in mes:
        if day:
            print(f"{str(d):>2}", end = " ")
        else:
            print(f"{" ":>2}", end = " ")
        contador += 1
        if contador % 7 == 0:
            print()
            contador = 0
    print()
    print(f"{"-"*len(semana)*4}")
    return None
    
def main():
    mes = int(input("Ingrese el numero de mes: "))
    anio = int(input("Ingrese el año: "))
    dia = diadelasemana(1,mes,anio)
    if mes in treintayuno:
        dias = 31
    elif mes in treinta:
        dias = 30
    elif not anio % 4 and (anio % 100 or not anio % 400):
        dias = 29
    else:
        dias = 28
    listames = elmes(dia,dias)
    calendario(listames,mes,anio)
    return None

treintayuno = (1,3,5,7,8,10,12)
treinta = (4,6,9,11)
meses = ("ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE"
         "OCTUBRE","NOVIEMBRE","DICIEMBRE")
semana = ("LUNES","MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO")
main()

# 9
import random
def cosecha(n):
    lista = []
    for i in range(n):
        lista.append(randint(150,350))
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