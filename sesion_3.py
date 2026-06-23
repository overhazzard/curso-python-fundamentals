"""Crea una función llamada calcularPromedio que reciba 3 notas y devuelva el promedio
- Usa def para definirla
- Recibe 3 parámetros (una por nota)
- Calcula el promedio dentro de la función
- Usa return para devolver el resultado
Llámala e imprime el resultado"""

"""def calcular_promedio(notas):
    return sum(notas) / len(notas)

notas = [15, 18, 20]
resultado = calcular_promedio(notas)
print(f"El promedio es: {resultado:.2f}")"""


"""def saludarUsuario(nombre):
    return print(f"Hola, {nombre}! Bienvenido/a al Curso de Programación en Python.")
nombreUsuario = input("Ingresa tu nombre: ")
saludarUsuario(nombreUsuario)

Desarrolla un programa en Python que haga lo siguiente:
- Pedir nombre y nota de 3 estudiantes
- Guardar cada uno en el archivo notas.txt con with open() en modo ‘a’
- Leer el archivo al final y mostrar el contenido en pantalla"""

"""for 0 in range(3):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    nota = input(f"Ingrese la nota de {nombre}: ")
    with open("notas.txt", "a") as archivo:
        archivo.write(f"{nombre}: {nota}\n")

print("\nContenido del archivo:")
with open("notas.txt", "r") as archivo:
    print(archivo.read())"""

"""Mini Registro de Gastos con Archivo:
- Una función agregar_gasto(descripcion, monto) que reciba y muestre el gasto
- Una función guardar_gasto() que lo escriba en gastos.txt con with open() en modo 'a'
Un bucle que pida al usuario 3 gastos y los registre usando las dos funciones
Al final leer el archivo completo y mostrar el resumen en pantalla"""

def agregar_gasto(descripcion, monto):
    print(f"Gasto registrado: {descripcion} - S/. {monto:.2f}")

def guardar_gasto(descripcion, monto):
    with open("gastos.txt", "a") as archivo:
        archivo.write(f"{descripcion}: S/. {monto:.2f}\n")

for i in range(3):
    descripcion = input(f"Descripción del gasto {i + 1}: ")
    monto = float(input(f"Monto: S/. "))
    agregar_gasto(descripcion, monto)
    guardar_gasto(descripcion, monto)

print("\nResumen de gastos guardados")
with open("gastos.txt", "r") as archivo:
    print(archivo.read())



