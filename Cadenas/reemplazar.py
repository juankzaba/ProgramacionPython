# Programa: Reemplazar textos en Python

mensaje = 'Hola Mundo, Mundo'

# Reemplazr TODAS las apariciones
nuevo = mensaje.replace('Mundo', 'Python')
print(nuevo) #Salida: HOLA Python, Python

# Reemplazar solo UNA vez
uno_sola = mensaje.replace('Mundo', 'Dev', 1)#Salida: 'Hola Dev, Mundo'
print(uno_sola)
uno_sola = mensaje.replace('Mundo', 'Dev', 2)
print(uno_sola)