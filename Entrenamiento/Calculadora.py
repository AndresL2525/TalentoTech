# importamos libreria
import math


# Titulo
def Show_title():
    print("\n==== CALCULADORA CIENTÍFICA ====\n")


# Menu
def mostrar_menu():
    print()
    print("MENU:")
    print("1: Sumar (+)")
    print("2: Restar (-)")
    print("3: Multiplicar (*)")
    print("4: Dividir (/)")
    print("5: Potencia (a^b)")
    print("6: Radicación ")
    print("7: Logaritmo (log)")
    print("8: seno (sen)")
    print("9: Coseno (cos)")
    print("10: Tangente (tan)")
    print()


# Capturamos los datos
def ingresa_datos():
    option = input("Ingrese la opción deseada: ").lower()

    if option in [
        "8",
        "sen",
        "seno",
        "sin",
        "9",
        "cos",
        "coseno",
        "10",
        "tangente",
        "tan",
    ]:
        print(f"¿Quieres calcular el/la {option} de 1 o 2 angulos")
        num_angulos = int(
            input("Escoga la cantida de angulos que quiere que se le calcule (1 o 2) ")
        )
        if num_angulos == 1:

            print("El ángulo debe ser en grados")
            numero_uno = float(input("Ingrese el primer número de la operación: "))
            numero_dos = None
        else:
            print("El ángulo debe ser en grados")
            numero_uno = float(input("Ingrese el primer número de la operación: "))
            numero_dos = float(input("Ingrese el segundo número de la operación: "))

    else:
        numero_uno = float(input("Ingrese el primer número de la operación: "))
        numero_dos = float(input("Ingrese el segundo número de la operación: "))

    return option, numero_uno, numero_dos


# definimos las operaciones
def calcular_suma(numero_uno, numero_dos):

    suma = numero_uno + numero_dos
    return suma


def calcular_resta(numero_uno, numero_dos):
    return numero_uno - numero_dos


def calcular_multiplicacion(numero_uno, numero_dos):
    return numero_uno * numero_dos


def calcular_division(numero_uno, numero_dos):
    return numero_uno / numero_dos


def calcular_potencia(numero_uno, numero_dos):
    return numero_uno**numero_dos


def calcular_radicacion(numero):
    return math.sqrt(numero)


def calcular_logaritmo(numero_uno, numero_dos):
    return math.log(numero_uno, numero_dos)


def calcular_seno(angulo_rad):
    return math.sin(math.radians(angulo_rad))


def calcular_coseno(angulo_rad):
    return math.cos(math.radians(angulo_rad))


def calcular_tangente(angulo_rad):
    return math.tan(math.radians(angulo_rad))


def procesar_y_mostrar_operacion(option, numero_uno, numero_dos):

    if option == "1" or option == "+" or option == "Sumar":
        print("Vamos a sumar(+) los dos valores ingresados:")
        resultado = calcular_suma(numero_uno, numero_dos)
        print("La suma es:", resultado)
    elif option == "2" or option == "-" or option == "Restar":
        print("Vamos a restar(-) los dos valores ingresados:\n")
        resultado = calcular_resta(numero_uno, numero_dos)
        print("Resultado=", resultado)
    elif option == "3" or option == "*" or option == "Multiplicar":
        print("Vamos a multiplicar(*) los dos valores ingresados:\n")
        resultado = calcular_multiplicacion(numero_uno, numero_dos)
        print("Resultado=", resultado)
    elif option == "4" or option == "/" or option == "Dividir":
        print("Vamos a dividir(/) los dos valores ingresados:\n")
        # VALIDANDO EL DENOMINADOR (debe ser diferente de cero)
        if numero_dos != 0:
            resultado = calcular_division(numero_uno, numero_dos)
            print("Resultado=", resultado)
        else:
            print("¡No es posible dividir entre cero!")
    elif option in ["5", "a^b", "potencia"]:
        resultado1 = calcular_potencia(numero_uno, numero_dos)
        print(
            f"Vamos a calcular la potenciación del primer termino {numero_uno} elevandolo al segundo numero {numero_dos}"
        )
        print(f"Resultado= {resultado}")

    elif option in ["6", "radicacion"]:
        resultado1 = numero_uno ** (1 / numero_dos)
        print(
            f"Vamos a obtener la raiz n_ésima del primer valor {numero_uno}, siendo n el segundo valor {numero_dos}"
        )
        print(f"Resultado= {resultado}")

    elif option in ["7", "log", "logaritmo"]:
        resultado1 = calcular_logaritmo(numero_uno, numero_dos)
        print(
            f"Vamos a calcular el logaritmo del primer valor {numero_uno}, cuya base es el segindo valor {numero_dos}"
        )
        print(f"Resultado= {resultado}")

    elif option in ["8", "sen", "seno", "sin"]:
        print("Vamos a calcular el coseno (cos) de los dos valores ingresados:\n")
        resultado1 = calcular_seno(numero_uno)
        print(f"El seno de {numero_uno}° es: = {resultado1}")
        if numero_dos is not None:
            resultado2 = calcular_seno(numero_dos)
            print(f"El seno  de {numero_dos}° es: = {resultado2}")


    elif option in ["9", "cos", "coseno"]:
        print("Vamos a calcular el coseno (cos) de los dos valores ingresados:\n")
        resultado1 = calcular_coseno(numero_uno)
        print(f"El coseno de {numero_uno}° = {resultado1}")
        if numero_dos is not None:
            resultado2 = calcular_coseno(numero_dos)
            print(f"El coseno de {numero_dos}° = {resultado2}")


    elif option in ["10", "tangente", "tan"]:
        print("Vamos a calcular la tangente (tan):")
        resultado1 = calcular_tangente(numero_uno)
        print(f"La Tangente de {numero_uno}° = {resultado1}")
        if numero_dos is not None:
            resultado2 = calcular_tangente(numero_dos)
            print(f"La Tangente de {numero_dos}° = {resultado2}")

def llamar_funciones():

    Show_title()
    mostrar_menu()
    option, numero_uno, numero_dos = ingresa_datos()
    procesar_y_mostrar_operacion(option, numero_uno, numero_dos)


# EJECUCIÓN DEL PROGRAMA CON BUCLE
while True:
    llamar_funciones()

    continuar = input("\n¿Deseas realizar otra operación? (si o no): ").lower()
    if continuar != "si":
        print("¡Gracias por usar la calculadora científica!")
        break
