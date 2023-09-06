# main.py

import calculadora.operaciones as oper
import calculadora.comparaciones as comp
import calculadora.secuencias as seq
import calculadora.factoriales as fact
import calculadora.utilidades.matematicas as util

while True:
    print("\nMenú de Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    print("6. Mayor")
    print("7. Menor")
    print("8. Igual")
    print("9. Diferente")
    print("10. Serie Fibonacci")
    print("11. Factorial")
    print("12. Mínimo Común Múltiplo")
    print("13. Máximo Común Divisor")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "0":
        print("Hasta luego!")
        break
    elif opcion == "1":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = oper.suma(a, b)
        print("Resultado:", resultado)
    elif opcion == "2":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = oper.resta(a, b)
        print("Resultado:", resultado)
    elif opcion == "3":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = oper.multiplicacion(a, b)
        print("Resultado:", resultado)
    elif opcion == "4":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = oper.division(a, b)
        print("Resultado:", resultado)
    elif opcion == "5":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = oper.modulo(a, b)
        print("Resultado:", resultado)
    elif opcion == "6":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = comp.mayor(a, b)
        print("Resultado:", resultado)
    elif opcion == "7":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = comp.menor(a, b)
        print("Resultado:", resultado)
    elif opcion == "8":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = comp.igual(a, b)
        print("Resultado:", resultado)
    elif opcion == "9":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = comp.diferente(a, b)
        print("Resultado:", resultado)
    elif opcion == "10":
        n = int(input("Ingrese el valor de n para la serie Fibonacci: "))
        resultado = seq.fibonacci(n)
        print("Resultado:", resultado)
    elif opcion == "11":
        n = int(input("Ingrese un número para calcular su factorial: "))
        resultado = fact.factorial(n)
        print("Resultado:", resultado)
    elif opcion == "12":
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        resultado = util.mcm(a, b)
        print("Resultado:", resultado)
    elif opcion == "13":
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        resultado = util.mcd(a, b)
        print("Resultado:", resultado)
    else:
        print("Opción no válida. Intente nuevamente.")
