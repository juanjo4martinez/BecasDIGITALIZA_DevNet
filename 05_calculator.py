# Mensaje de bienvenida
print("""
===============================
=    CALCULADORA EN PYTHON    =
===============================
""")

# Introducir el primer número (solo se aceptan enteros o decimales)
while True:
    try:
        num1 = float(input('Primer número: '))
    except ValueError:
        print("*** Valor incorrecto (solo se aceptan números enteros o decimales)")
        continue
    else:
        break 

# Introducir el segundo número (solo se aceptan enteros o decimales)
while True:
    try:
        num2 = float(input('Segundo número: '))
    except ValueError:
        print("*** Valor incorrecto (solo se aceptan números enteros o decimales)")
        continue
    else:
        break

# Definir funciones para cada operación matemática
def suma():
    return num1 + num2

def resta():
    return num1 - num2

def multi():
    return num1 * num2

def division():
    return num1 / num2    

def expo():
    return num1 ** num2

# Crear diccionario con las diferentes operaciones
operaciones = { '1':suma(), '2':resta(), '3':multi(), '4':division(), '5':expo() }

# Mostrar menú para elegir la operación
print("""
=====================
=    OPERACIONES    =
=====================

1. Suma
2. Resta
3. Multiplicación
4. División
5. Exponencial""")

# Para valores que no sean números, mostrar un mensaje y repetir bucle
while True:
    try:
        seleccion = int(input("""
==========================
=    ELIGE UNA OPCIÓN    =
==========================

"""))
    except ValueError:
       print("\n*** Opción incorrecta (no se admiten caracteres) ***")
       continue
    else:
        break

# Para valores que no estén en el rango 1 a 5, mostrar un mensaje y repetir bucle
while (seleccion < 1 or seleccion > 5):
    try:
        seleccion = int(input("""
*** Opción incorrecta (solo se admiten valores del 1 al 5) ***

==========================
=    ELIGE UNA OPCIÓN    =
==========================

"""))
    except ValueError:
        continue
        
# Mostrar resultado de la operación
print("""
===================
=    RESULTADO    =
===================
""")

if seleccion == 1:
    print(num1,"+",num2,"=",operaciones['1'])
elif seleccion == 2:
    print(num1,"-",num2,"=",operaciones['2'])
elif seleccion == 3:
    print(num1,"*",num2,"=",operaciones['3'])
elif seleccion == 4:
    print(num1,"/",num2,"=",operaciones['4'])
elif seleccion == 5:
    print(num1,"**",num2,"=",operaciones['5'])

print("""
===================
""")
