
"""PROYECTO FINAL FASE 1: Gestor de Gastos
Hoy construyes las funciones base del Gestor de Gastos Personal. 
Crea un archivo gestor.py con las siguientes funciones:
- agregar_gasto(descripcion, monto) que reciba y muestre el gasto
- guardar_gasto(descripcion, monto) que lo escriba en gastos.csv
- mostrar_gastos() que lea el archivo y muestre todos los registros"""

import csv
def agregar_gasto(descripcion, monto):
    print(f"Gasto registrado: {descripcion} - S/. {monto:.2f}")

def guardar_gasto(descripcion, monto):
    with open("gastos.csv", "a", newline="") as archivo:
        escribir = csv.writer(archivo)
        escribir.writerow([descripcion, monto])

def mostrar_gastos():
    print("\n" + "=" * 30)
    print("     REGISTRO DE GASTOS")
    print("=" * 30)

    with open("gastos.csv", "r") as archivo:
        archivo_csv = csv.reader(archivo)
        for fila in archivo_csv:
            print(f"{fila[0]:20} S/. {float(fila[1]):.2f}")
    print("=" * 30)