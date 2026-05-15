'''

*** Calculo Area y Perimetro de un Rectángulo

Se solicita calcular el área y perímetro de un rectángulo aplicando las siguien te fórmulas:

area = base * altura
perimietro = 2 * (base + alura)
'''

print(f'*** Calculo Area y Perimetro de un Rectángulo ***')

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Realizamos los calculos
area = base * altura
perimietro = 2 * (base + altura) # Aplicamos la prececedencia de operaciones

print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimietro}")

