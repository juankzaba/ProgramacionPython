print(' *** Break y Continue **')

# Ejemplo con Break
print('Palabra Break')
for numero in range(1, 10):
    if numero % 2 == 0: # Número par
        print(numero)
        break #Salimos del ciclo completamente

# Ejemplo con Continue
print('\nPalabra Continue')
for numero in range(1, 10):
    if numero % 2 == 1: # Número impar
        print(numero)
        continue
    print(numero) # Numero Pares