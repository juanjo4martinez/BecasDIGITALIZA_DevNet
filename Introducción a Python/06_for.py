# Crear las listas 'nombres' (contiene 5 nombres) y 'selected' (vacía)
nombres = ['Juan','María','Miguel','Jessica','Pedro']
selected = []

# Bucle FOR que imprime el nombre recorrido en cada iteración
# Si 'a' existe en alguno de los nombres, añade ese nombre a la lista 'selected'
for n in nombres:
    print("El nombre recorrido en esta iteración es",n)
    if 'a' in n:
        selected.append(n)

# Imprimir por pantalla la lista 'selected'
print("Nombres que contienen la letra 'a':",selected)
