from random import randint

print('***Juego de Adivinanzas***')

numero_secreto = randint(1, 50)
intentos = 0
adivinanza = None
INTENTOS_MAXIMOS = 5

while adivinanza != numero_secreto and intentos < INTENTOS_MAXIMOS:
    adivinanza = int(input("Adivine el numero secreto (1-50): "))
    #Agregamos una ayuda para orientar al jugador
    if adivinanza < numero_secreto:
        print('El numero secreto es mayor')
    elif adivinanza > numero_secreto:
        print('El numero secreto es menor')
    #Incrementamos la variable de intentos
    intentos+= 1
# Conclusión del juego
if adivinanza == numero_secreto:
    print(f"Felicidades adivinaste el numero secreto en {intentos} intentos")
else:
    print(f"Lo siento, has agotado tus intentos máximos: {INTENTOS_MAXIMOS}")
    print(f"El número secreto era: {numero_secreto}")