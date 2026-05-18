
'''Crear un sistema de reserva de hoteles que contenga la siguiente
 informaicon de una reserva

. Nombre del cliente
. Días de estancia
. Tarifa diaria
. Indicar si el cuarto tiene vista al mar

. Después mandar a imprimir los valores de cada variable

- Hacer algunos cambios y re-imprimir

El resultado debe ser similar al siguiente

*** Sistema de Reserva de Hoteles ***

Cliente: Laura Martinez
Días de estancia: 5
Tarifa diaria: 1200.0
Habitación con vista al mar? True
'''

#Declaración de variables

nombre_cliente = 'Laura Martinez'
dias_estancia = 5
tarifa_diaria = 1200.0
vista_mar = True

# Mostrar el detalle de la reserva

print('*** Sistema de Reserva de Hoteles ***')
print('Cliente:', nombre_cliente)
print('Días de estancia:', dias_estancia)
print('Tarifa diaria:', tarifa_diaria)
print('Habitación con vista al mar?:', vista_mar)

# Realizamos algunas modificaciones de la reserva

dias_estancia = 7
tarifa_diaria = 1000.0
vista_mar = False

# Mostrar el detalle de la reserva

print('*** Sistema de Reserva de Hoteles ***')
print()
print('Cliente:', nombre_cliente)
print('Días de estancia:', dias_estancia)
print('Tarifa diaria:', tarifa_diaria)
print('Habitación con vista al mar?:', vista_mar)

