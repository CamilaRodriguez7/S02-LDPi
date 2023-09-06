def mostrar_menu():
    print("Calculadora Simple")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

def seleccionar_opcion():
    opcion = input("Seleccione una opción: ")
    return opcion

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def iniciar_menu():
    while True:
        mostrar_menu()
        opcion = seleccionar_opcion()

        if opcion == '1':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = sumar(num1, num2)
            print("El resultado de la suma es:", resultado)
        elif opcion == '2':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = restar(num1, num2)
            print("El resultado de la resta es:", resultado)
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
