'''Sistema generador ID Unico

Con los datos recibidos el sistema deberá realizar lo siguiente:

1. Del valor recibido de nombre, usar solo las 2 primeras letras y convertirlas
a mayusculas

2. Del valor del apellido, usar las 2 primeras letras y convertirlas a mayusculas

3. Del valor de año, tomar las 2 ultimos digitos.

Además el sistema deberá generar un valor aleatorio de 4 digitos, con ayuda de la funcion
randint

Finalmente, con los datos obtenidos generar un ID unico uniendo los valores como sigue

Ejemplo: Nombre - Juan - JU
Apellido - Perez -PE
Año nacimiento - 1995 - 95
Valor aleatorio - randint - 7326

Resultado ID Unico: JUPE957326

*** SISTEMA GENERADOR DE ID UNICO ***
Cual es tu nombre? Juan
Cual es tu apellido? Perez
Cual es tu año de nacimiento (YYYY) 1995

Hola Juan,
Tu nuevo número de identificación (ID) generado por el sistema es:
JUPE955475
Felicidades!

'''
from random import randint

print(f"*** SISTEMA GENERADOR DE ID UNICO ***")

nombre = input("Cuál es tu nombre: ")
apellido = input("Cuál es tu apelllido: ")
anio_nacimiento = input("Cuál es el año de tu nacimiento (YYYY): ") # Y - year

# Normalizar los valores
nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
anio_nacimiento_2 = anio_nacimiento.strip().upper()[2:]# También puede ser [2:4]

# Generar el valor aleatorio
aleatorio = randint(1000, 9999)
id_unico = f"{nombre_2}{apellido_2}{anio_nacimiento_2}{aleatorio}"

print(f'''\nHola {nombre},
    Tu nuevo número de identificación (ID) generado por el sistema es:
    {id_unico}
    Felicidades!


''')