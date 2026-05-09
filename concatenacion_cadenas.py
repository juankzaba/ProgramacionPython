# Programa: Ejemplo de concatenación de cadenas

#1 Usando el operador
nombre = 'Lucia'
apellido = 'Uribe'
nombre_completo = nombre + " " + apellido
print("Usando + :" + nombre_completo)

# 2.  Usando el método print
edad = 28
print("Usando comas:", "Nombre", nombre_completo, ",Edad:", edad)

# 3. Usando f-string
ciudad = 'Barcelona'
pais = 'España'
profesion = ' ingeniera'
presentacion = f"Hola, soy {nombre_completo}, tengo {edad + 1} años y soy {profesion} en {ciudad}, {pais}"
print(presentacion)