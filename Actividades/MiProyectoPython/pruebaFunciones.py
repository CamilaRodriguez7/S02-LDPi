import funcionesComparacion

# probando las funciones
resultado_maximo = funcionesComparacion.hallar_maximo(10, 20)
print("El máximo es:", resultado_maximo)

resultado_minimo = funcionesComparacion.hallar_minimo(10, 20)
print("El mínimo es:", resultado_minimo)

resultado_igualdad = funcionesComparacion.son_iguales(10, 10)
print("Son iguales:", resultado_igualdad)

resultado_diferencia = funcionesComparacion.son_diferentes(10, 20)
print("Son diferentes:", resultado_diferencia)

from funcionesIngreso import verificar_numero
verificar_numero("abc")  # Esto debería mostrar un mensaje de error.
verificar_numero("123")  # Esto debería ejecutarse sin errores.

import menu
menu.iniciar_menu()