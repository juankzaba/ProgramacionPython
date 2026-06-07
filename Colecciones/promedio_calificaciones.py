print('*** Promedio de calificaciones ***')

total_calificaciones = int(input("Proporciona el número de calificaciones a evaluar: "))
calificaciones = []

# Iterar las calificacione
for indice in range(total_calificaciones):
    calificacion = float(input(f"Califiación[{indice}]: "))
    calificaciones.append(calificacion)

# Imprimimos las califaciones proporcionadas
print(f"\nLas calificaciones proporcionadas son: {calificaciones}")

# Calculamos el promedio de las calificaciones
suma_calificacion = sum(calificaciones)
promedio = suma_calificacion / total_calificaciones
print(f"\nPromedio de las calificacioens: {promedio:.2f}")








