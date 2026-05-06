#Ejemplo: Cadenas inmutables

animal = 'Gato'
# animal[4] = 's' #Provoca un error
#CORRECTO: Concatenar (Sumar)
#Tomamos'Gato' + 's' y lo guardamos en una nueva variable
plural = animal +'s'
print(animal)#salida: 'Gato' (Intacto)
print(plural) # Salida: 'Gatos' (Nuevo objeto)

#Otra forma de concatenarlo
plural = f"{animal}s"
print(plural) # Salida: 'Gatos' (Nuevo objeto)
