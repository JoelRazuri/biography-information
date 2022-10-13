"""
    Pregunte a un usuario su información personal en una sola ronda de preguntas. Luego hay que verificar que la información que se ha ingresado sea válida. 
    Finalmente, se imprime un resumen de toda la información que ha sido ingresada.

    Por ejemplo: ¿Cuál es su nombre? Si el usuario ingresa *, hay que indicar que la entrada es incorrecta y se pide que se ingrese correctamente un nombre válido.

    Cuando se introduce todo correctamente, se muestra un resumen como el que aparece a continuación:

        - Nombre: John Doe
        - Fecha de nacimiento: Jan 1, 1954
        - Dirección: 24 fifth Ave, NY
        - Metas personales: To be the best programmer there ever was
"""

import os 


def mostrar_datos(datos_persona):

    nombre,fecha_nacimiento,direccion,metas = datos_persona

    os.system("cls")
    print(f"- Nombre: {nombre}")
    print(f"- Fecha de nacimiento: {fecha_nacimiento}")
    print(f"- Dirección: {direccion}")
    print(f"- Metas personales: {metas}")
    print()
    input("Ingrese cualquier tecla para salir...")


def validar_nombre(nombre):

    continuar = True
    i = 0

    if not nombre:
        input("El campo no puede estar vacio. Ingrese un nombre...")
        continuar = False
    else:
        while i<len(nombre) and continuar:
            if not ((nombre[i]>='A' and nombre[i]<='Z') or (nombre[i]>='a' and nombre[i]<='z') or (nombre[i]==" ")):
                continuar = False
                input("Ingrese un nombre valido. Solo caracteres alfabeticos...")
            i+=1

    return continuar

def validar_formato(fecha_nacimiento):

    continuar = True
    i = 0

    while continuar and i<len(fecha_nacimiento):
        if (i==2 or i==5):
            if not fecha_nacimiento[i]=='/':
                continuar = False
        else:
            if not (fecha_nacimiento[i]>='0' and fecha_nacimiento[i]<='9'):
                continuar = False
        i+=1


    if continuar:
        dias,mes,ano = fecha_nacimiento.split("/")
        if len(ano)<4:
            continuar = False

    return continuar

def existe_fecha(fecha_nacimiento):

    dia,mes,ano = fecha_nacimiento.split("/")
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    dias=cantidad_dias(mes,ano)
    
    if (dia<=dias and ano<2008 and (mes>=1 and mes<=12)):
        fecha=True
    else:
        fecha=False

    return fecha

def es_bisiesto(ano):
    # Dado un ano indicar si es bisiesto.

    if ano%4==0 and (ano%100!=0 or ano%400==0):
        bisiesto=True
    else:
        bisiesto=False

    return bisiesto

def cantidad_dias(mes,ano):
    # Dado un mes y un ano, devolver la cantidad de días correspondientes.

    if mes==2:
        if es_bisiesto(ano)==True:
            dias=29
        else:
            dias=28
    elif mes==4 or mes==6 or mes==9 or mes==11:
        dias=30
    else:
        dias=31

    return dias  


def validar_fecha(fecha_nacimiento):

    if not fecha_nacimiento:
        booleano = False
        input("El campo no puede estar vacio. Ingrese una fecha...")  
    else:
        formato = validar_formato(fecha_nacimiento)

        if formato:
            booleano = existe_fecha(fecha_nacimiento)
            if not booleano:
                print("Ingrese una fecha valida.")
                input()
        else:
            booleano = False
            print("Formato de fecha no valido.")
            input()

    return booleano



def ingresar_datos(datos_persona):

    nombre_valido = False
    fecha_valido = False

    while not nombre_valido:
        os.system("cls")
        nombre = input("Ingrese su nombre: ")
        nombre_valido = validar_nombre(nombre)
    datos_persona.append(nombre)
    
    while not fecha_valido:
        os.system("cls")
        fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
        fecha_valido = validar_fecha(fecha_nacimiento)
    datos_persona.append(fecha_nacimiento)
    
    os.system("cls")
    direccion = input("Ingrese la dirección: ")
    datos_persona.append(direccion)
    
    os.system("cls")
    metas = input("Ingrese su metas personales: ")
    datos_persona.append(metas)



def main():

    datos_persona = []

    ingresar_datos(datos_persona)
    mostrar_datos(datos_persona)


if __name__=="__main__":
    main()
