from utilidades import impuestos as imp
from utilidades import calculos

monto = int(input("Introduzca un monto entero: "))  # Llama función definida en el módulo "impuestos"
print("El impuesto IVA de 12%:", imp.impuesto_iva12(monto))

suma = int(input("Introduzca un monto entero a sumar: "))  # Llama función definida en el módulo "calculos"
print("La suma total es:", calculos.suma_total(suma))