import sys
sys.stdout.reconfigure(encoding='utf-8')
# -*- coding: utf-8 -*-
edad = 20
#print(f"En 5 años tendrás {edad + 5} años")


# =============================
#IF/ELIF/ELSE
#Ejercicio 1: Pide la edad del usuario e imprime si es mayor de edad, adolescente o menor de edad.

"""edad = int(input("¿Cuál es tu edad? "))
if edad >= 30:
    print("Eres un adulto")
elif edad >= 18 and edad < 30:
    print("Eres mayor de edad")
elif edad >= 12 and edad < 18:
    print("Eres adolescente")
else:
    print("Eres menor de edad")"""

#Ejercicio 2: Pide la nota de un estudiante (0-20) y muestra Excelente, Aprobado o Desaprobado. 
"""nota = int(input("¿Cuál es tu nota? "))

if nota >= 18 and nota <= 20:
    print("Excelente, tienes una buena nota")
elif nota >= 11 and nota < 18:
    print("Aprobado, tienes una nota regular")
else:
    print("Desaprobado, debes estudiar más")"""

#Ejercicio 3: Declara una variable con un número entero y muestra si es par o impar.
"""numero = int(input("Ingresa un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:    
    print(f"El número {numero} es impar.")"""

# =============================
#ITERAR
#BUCLES: FOR/WHILE
#Ejercicio 1: Usa un bucle for para imprimir los números del 1 al 10.
#for i in range(1, 11):
    #print(i)

#Ejercicio 2: Pide números al usuario uno por uno y sumalos. Para cuando el usuario escriba 0 y muestra el total. 
"""total = 0
while True:
    numero = int(input("Ingresa un número entero (Escribe 0 para terminar el programa): "))
    if numero == 0:
        break
    total += numero
print(f"El total es: {total}")"""

# =============================
#LISTAS, TUPLAS Y DICCIONARIOS
#Ejercicio 1: Crea una lista con 4 frutas, agrega una más, elimina la primera e imprime la lista final. 
"""frutas = ["manzana", "pera", "naranja", "plátano", "manzana", "naranja"]
print(frutas)
frutas.append("uva")
print(frutas)
frutas.remove("manzana")
print(frutas)"""

#Ejercicio 2: Crea un diccionario con tu nombre, edad y ciudad. Actualiza tu edad e imprime todos los valores.
"""miPerfil = { "nombre" : "Cristopher", "edad" : 27, "ciudad" : "Lima"}
print(miPerfil)
miPerfil["edad"] = 22
miPerfil["nombre"] = "Wilberd"
print(miPerfil)
print(f"Nombre: {miPerfil['nombre']}")
print(f"Edad: {miPerfil['edad']}")
print(f"Ciudad: {miPerfil['ciudad']}")"""


#Ejercicio3: Crea una tupla con las coordenadas (latitud, longitud) de tu ciudad e imprime un mensaje indicando su ubicación
"""coordenadas = (-12.0211, -77.0347, 22233232)
print(f"Latitud: {coordenadas[0]}")
print(f"Longitud: {coordenadas[1]}")
print(f"Item 3: {coordenadas[2]}")
print(f"Ubicación: Lima, San Martín de Porres está en las coordenadas {coordenadas[0]}, {coordenadas[1]}")"""

#PROCESAMIENDO DE DATOS
#Tienes una lista de precios de productos y necesitas calcular automáticamente el resumen del día
"""Recorre cada precio de la lista con un bucle for
Sumar cada precio al total acumulado
calcular el promedio dividiendo el total entre la cantidad de productos
Encontrar el precio más alto con max()
Encontrar el precio más bajo con min()
Mostrar todo formateado con 2 decimales"""

precios = [15.50, 8.00, 22.50, 5.75, 30.00]
total = 0
for precio in precios:
    total += precio
promedio = total / len(precios)
precio_max = max(precios)
precio_min = min(precios)

print(f"Total: ${total:.2f}")
print(f"Promedio: ${promedio:.2f}")
print(f"Precio más alto: ${precio_max:.2f}")
print(f"Precio más bajo: ${precio_min:.2f}")


#Ejercicio Final de la Sesión: 
"""
Pedir el nombre y nota de 4 estudiantes
Guardar los datos en una estructura (lista o diccionario)
Calcular el promedio del salón
Mostrar quién aprobó y quien desaprobó (aprobado > 11)
Mostrar la nota más alta y más baja
"""

notas = {}

for i in range(4):
    nombre = input(f"Nombre del estudiante {i+1}: ")
    nota = int(input(f"Nota del estudiante {i+1}: "))
    notas[nombre] = nota

print("=" * 30)
print("REPORTE DEL SALON")
print("=" * 30)

for nombre, nota in notas.items():
    if nota > 11:
        print(f"{nombre} aprobó con una nota de {nota}.")
    else:
        print(f"{nombre} desaprobó con una nota de {nota}.")

promedio = sum(notas.values()) / len(notas)
print(f"Promedio del salón: {promedio:.1f}")
print(f"Nota más alta: {max(notas.values())}")
print(f"Nota más baja: {min(notas.values())}")