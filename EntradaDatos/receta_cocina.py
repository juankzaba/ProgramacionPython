'''

Crear un programa para solicitar algunos valores importantes para una receta de cocina

Los valores que debe introducir el usuario son:
Nombre de la receta
Ingredietes
Tiempo de preparación(en minutos)
Dificultad('Facil, media, alta'

Mandar a imprimir la receta de tal forma que quede asi

*** RECETA COCINA ***

----------------

Ingresa el nombre: plato arcoiris
Ingresa los ingredientes: quinoa, col roja, aguacate, zanahoria y aceite oliva
Ingrese el tiempo de preparación (min): 10
Ingrese la dificultad: Facil

'''

print(f"*** RECETA COCINA ***")

nombre_receta = input("Ingresa el nombre: ")
ingredientes = input("Ingresa los ingredientes: ")
tiempo_preparacion = int(input("ngrese el tiempo de preparación (min): "))
dificultad_preparacion = input("Ingrese la dificultad: ")
print('--------------')

print(f"Nombre del plato: {nombre_receta}")
print(f"Ingredientes: {ingredientes}")
print(f"Tiempo de preparación: {tiempo_preparacion}")
print(f"Dificultad: {dificultad_preparacion}")



