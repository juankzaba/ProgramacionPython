print('*** Playlist de canciones ***')

# Creamos la lista vacía
lista_reproduccion = []

# Empezamos a agregar canciones
lista_reproduccion.append('Hotel California - Eagles')
lista_reproduccion.append('Staying Alive - Bee Gees')
lista_reproduccion.append('Dream on - Aerosmith')

# Ordenar la lista en orden alfabético método sort
lista_reproduccion.sort()

# Mostrar la lista de canciones
print(f"\n Lista de Reproduccción en orden alfabético: ")
print(lista_reproduccion)

# Mostrar la lista, iterando sus elementos
print('\nIteramos el playlist')
for cancion in lista_reproduccion:
    print(f'- {cancion}')