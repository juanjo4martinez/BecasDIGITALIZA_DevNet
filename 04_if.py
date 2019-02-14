# Crear variable que almacena un número entero introducido por el usuario
numero = int(input("Introduce un número: "))

# Condicional 'if' - Según el número introducido, muestra si pertenece a un rango u otro
if numero < 20:
    print("El número es menor que 20","->",numero)
elif 20 < numero < 39:
    print("El número está entre 20 y 39","->",numero)
elif 40 < numero < 59:
    print("El número está entre 40 y 59","->",numero)
else:
    print("El número es mayor que 60","->",numero)
