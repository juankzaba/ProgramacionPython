print(' *** Dibujar Triángulo Simétrico ***')

numero_filas = int(input("Proporciona el número de filas: "))

# Iterar sobre cada fila del triángulo
for fila in range(1, numero_filas + 1):
    espacios_blaco = ' ' * (numero_filas - fila)
    asteriscos = '*' * (2 * fila -1)
    print(f"{espacios_blaco}{asteriscos}")
