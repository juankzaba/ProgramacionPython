'''SISTEMA DE EMPLEADO

Crea un programa para solicitar la información de un empleado, introducioendo
los datos por consola

Nombre empleado
Edad del empleado(Convertir a entero)
Salario del empleado (Convertir a flotante)
Es jefe de departamente (SI/NO)

'''

print("*** SISTEMA DE EMPLEADO ***")
nombre_empleado = input("Nombre del empleado: ")
edad_empleado = int(input("Edad del empleado: "))
salario_empleado = float(input("Salario del empleado: "))
es_jefe_departamento = input("Es jefe departamento (Si/No)?: ")

# Vamos a convertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower()=="si"

# Imprimir los valores del empleado
print(f"\nDatos del empleado")
print(f"Nombre: {nombre_empleado}")
print(f"Edad: {edad_empleado}")
# print(f"Salario: {salario_empleado}")
print(f"Salario = {salario_empleado:.2f}")
print(f"Es jefe de departamento: {es_jefe_departamento}")
