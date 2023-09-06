import sys
import os
import funcionesComparacion
from funcionesIngreso import verificar_numero
# Se obtiene la ruta de la carpeta de proyecto
ruta_proyecto = r"\Users\Camisa\Documents\MiProyectoPython"

# Se agrega la ruta de la carpeta de proyecto al sys.path
sys.path.append(ruta_proyecto)
print(funcionesComparacion.hallar_minimo(2,3))
# Ahora se puede importar los módulos utilizando rutas absolutas
