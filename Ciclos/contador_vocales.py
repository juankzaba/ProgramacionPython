'''Escribe un programa que declare una variable llamada cadena con el valor de "Hola Mundo".

Posteriormente usando un ciclo for, debe contar la cantidad de vocales presentes en la cadena y finalmente imprimir la cantidad de vocales encontradas (solo el número con la cantidad de vocales encontradas es el que se debe imprimir).'''

# Declarar la variable
# Agregar el ciclo for
# Imprimir la cantidad de vocales encontradas en la cadena


cadena = "Hola Mundo"
contador = 0

for letra in cadena:
    if letra.lower() in "aeiou":
        contador += 1

print(contador)