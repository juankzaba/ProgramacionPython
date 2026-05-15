'''
*** Valor Dentro de Rango

Solicitar al usuario un valor entre 0 y 5 e indicarle si el valor proporcionado está dentro de rango

Se deben definir 2 constantes, VALOR_MINIMO = 0 Y VALOR_MAXIMO = 5

Y debemos comprobar si el valor proporcionado se encuentra en el rango entre 0 y 5

Finalmente se debe imprimir: Valor dentro de rango: True/False

'''
from Operadores.dentro_rango_not import esta_dentro_de_rango

print('*** Valor Dentro de Rango')

VALOR_MINIMO_2 = 0
VALOR_MAXIMO_2 = 5

# solicitamos un valor entre o y 5
dato_2 = input(f"Proporciona un dato entre {VALOR_MINIMO_2} y {VALOR_MAXIMO_2}: ")

# Verificamos si el dato se encuentra dentro del rango
# esta_dentro_de_rango_ = dato_2 >= VALOR_MINIMO_2 and dato_2 <= VALOR_MAXIMO_2
esta_dentro_de_rango_ = VALOR_MINIMO_2 <= dato_2 <= VALOR_MAXIMO_2
print(f"Valor está dentro de rango? {esta_dentro_de_rango_}")