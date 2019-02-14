# Crear variables con strings, integers y floats
listaStr = ["uno","dos","tres","cuatro"]
listaInt = [1,2,3,4]
listaFloat = ["uno",2,3.0,4.0]

# Imprimir por pantalla las listas
print(listaStr)
print(listaInt)
print(listaFloat)

# Crear variables con el último valor de cada lista
ultimoStr = listaStr[-1]
ultimoInt = listaInt[-1]
ultimoFloat = listaFloat[-1]

# Imprimir por pantalla las variables anteriores
print(ultimoStr)
print(ultimoInt)
print(ultimoFloat)

# Imprimir por pantalla las variables concatenadas (convirtiéndolas a strings) 
print("Variables concatenadas: "+ultimoStr+str(ultimoInt)+str(ultimoFloat))

# Crear el diccionario (directores:películas)
diccionario = {"George Lucas":"Star Wars","Peter Jackson":"El Señor de los Anillos"}

# Imprimir por pantalla el diccionario
print(diccionario)

# Imprimir por pantalla las claves del diccionario
print(diccionario.keys())

# Imprimir por pantalla los valores del diccionario
print(diccionario.values())
