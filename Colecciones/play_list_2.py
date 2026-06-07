print('*** Playlist de canciones Automáticas ***')

# Creamos la lista vacía
lista_reproduccion = []

numero_canciones = int(input("Cuántas canciones deseas agregar?: "))

# Iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f"Proporciona la canción {indice + 1}: ")
    lista_reproduccion.append(cancion)

# Ordenar la lista en orden alfabético método sort
lista_reproduccion.sort()

# Mostrar la lista, iterando sus elementos
print('\nIteramos el playlist')
for cancion in lista_reproduccion:
    print(f'- {cancion}')

# Hotel California - Eagles
# Staying Alive - Bee Gees
# Dream on - Aerosmith