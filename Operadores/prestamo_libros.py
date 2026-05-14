'''
Sistema Prestamo de Libros

Se pide crear un sistema para una biblioteca, la cual desea prestar libros

Si cumple con lcualquiera de las siguientes condiciones.

1. El usuario tiene credencia de estudiante
2. el usuario vivie a no más de 3km a la redonda

Si cumple con cualquiera de estas condicones dse le puede prestar el libro

'''
print(f"*** Sitema Préstamo de Libros ***")
DISTANCIA_PERMITIDA_KM = 3
tiene_credencial = input("Cuentas con credencial de estudiante (Si/No): ")
distancia_biblioteca_km = int(input("A cuántos kilometros vives de la biblioteca?: "))

es_elegible_prestamo = (distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM
                         and tiene_credencial.strip().lower() == 'si') # Al dar enter antes de and cuándo está en una sola línea pycharm automaticamente abre paréntesis

print(f"Tienes acceso al descuento VIP?: {es_elegible_prestamo}")