# TP 1 Ejercicio 8
# Algoritmos y estructuras de datos
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
            print(f"{str(day):>2}", end = " ")
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