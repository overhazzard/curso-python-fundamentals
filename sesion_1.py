#print("¡Hola mundo!")
#print("¡Bienvenido a Python Fundamentals!")
#print("¡Vamos a aprender Python juntos!")

# Ejercicio 1: Crea un archivo llamado hola.py y haz que Python imprima tu nombre, tu ciudad y una frase que describa cómo te sientes hoy. 
#print("Mi nombre es Wilberd Espino.")
#print("Vivo en San Martín de Porres, Lima, Perú.")#
#print("Hoy me siento muy emocionado por el inicio del curso de Python Fundamentals.")

#Ejercicio 2: Haz que Python imprima una tarjeta de bienvenida con tu nombre en el centro, usando líneas de = arriba y abajo. 
#print("=" * 30)
#print("Bienvenido, Wilberd Espino!")
#print("=" * 30)

#cammelCase
#nombreCompleto = "Wilberd Espino"
#print(nombreCompleto)

#snake_case
#nombre_completo = "Cristopher Gamboa Espino"
#print(nombre_completo)

#Ejercicio 2: Crea variables para guardar tu nombre, edad, altura y si actualmente estás trabajando. Imprime cada una en una línea distinta. 
#altura = 1.77
#edad = 27
#estoyTrabajando = True
#print("Mi nombre es: ", nombreCompleto)
#print("Tengo", edad, "años.")
#print("Mi altura es:", altura, "metros.")
##print("Estoy trabajando:", estoyTrabajando)

#Ejercicio 3: Crea las mismas variables del ejercicio anterior y usa type() en cada una. ¿Qué tipo reconoce Python para cada dato? 
#nombre = "Cristopher"
#edad = 72
#altura = 1.50
#estoyTrabajando = True

#print(type(nombre))  # Salida: <class 'str'>
#print(type(edad))    # Salida: <class 'int'>
#print(type(altura))  # Salida: <class 'float'>
#print(type(estoyTrabajando))  # Salida: <class 'bool'>

#Ejercicio 1: Declara dos números enteros a elección y muestra su suma, resta, multiplicación, división, división entera y módulo. Etiqueta cada resultado. 
#numero1 = 15
#numero2 = 2

#print(f"Suma: {numero1 + numero2}")
#print(f"Resta: {numero1 - numero2}")
#print(f"Multiplicacion: {numero1 * numero2}")
#print(f"Division: {numero1 / numero2}")
#print(f"Division Entera: {numero1 // numero2}")
#print(f"Modulo: {numero1 % numero2}")

#Ejercicio 2: Pide al usuario el precio de un producto y la cantidad que quiere comprar. Calcula el total a pagar y muéstralo en consola.. 
#precio = float(input("¿Cuál es el precio del producto? S./ "))
#cantidad = int(input("¿Cuántas unidades desea comprar?"))
#total = precio * cantidad
#print(f"El total a pagar es: S./ {total}")

# Código con errores
#nombre = input("¿Tu nombre? ")
#print(f"Hola {nombre}")
#edad = int(input("¿Tu edad? "))
##print(f"En 5 años tendrás {edad + 5} años")#

#Desarrolla un mini cajero que haga lo siguiente: 
#Pida el nombre del usuario y su saldo actual
#Pida dos gastos realizados durante el día
#Calcule el total gastado y el saldo restante
#Calcule qué porcentaje del saldo se gastó
#Muestre un resumen final con todos los datos formateados

# =============================
# MI CAJERO PERSONAL
# =============================

"""print("=" * 35)
print("         MI CAJERO PERSONAL")
print("=" * 35)

nombreUsuario = input("¿Cual es tu nombre?")
print(f"Hola {nombreUsuario}, bienvenido a tu cajero.")
saldoActual = float(input("¿Cuánto dinero tienes disponible en tu cuenta? S/. "))
print(f"Tu saldo actual es: S/. {saldoActual}")

gasto1 = float(input("Ingresa tu primer gasto del día: S/."))
gasto2 = float(input("Ingresa tu segundo gasto del día: S/."))

totalGastado = gasto1 + gasto2
saldoFinal = saldoActual - totalGastado
porcentajeGastado = (totalGastado / saldoActual) * 100

print("=" * 35)
print("         RESUMEN DEL DÍA")
print("=" * 35)

print(f"Gasto 1: S/. {gasto1}")
print(f"Gasto 2: S/. {gasto2}")
print(f"Total gastado: S/. {totalGastado:.2f}")
print(f"Saldo final: S/. {saldoFinal}")
print(f"Porcentaje gastado: {porcentajeGastado:.2f}%")"""