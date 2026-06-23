"""import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#DATOS DE CORREO
mi_correo = "pha.edutech@gmail.com"
mi_contraseña="bncj xxga xxqx nhxi"

#CREAR EL MENSAJE
mensaje = MIMEMultipart()
mensaje["From"] = mi_correo
mensaje["To"] = mi_correo
mensaje["Subject"] = "Mi primer correo automático con Python 2"

cuerpo = "Este correo fue enviado automáticamente con Python y smtplib 2"
mensaje.attach(MIMEText(cuerpo, "plain"))

#Enviar
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()
        servidor.login(mi_correo, mi_contraseña)
        servidor.send_message(mensaje)
    print("Correo enviado exitosamente")
except Exception as e:
    print(f"Error: {e}")"""

"""Menú interactivo con 4 opciones usando while True
- Consulta automática del tipo de cambio USD/PEN al iniciar
- Registro de gastos guardados en gastos.csv
Resumen con total, promedio, mayor y menor gasto
Equivalencia en dólares calculada en tiempo real"""

import requests
import csv

def obtener_tipo_cambio():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        respuesta = requests.get(url)
        datos = respuesta.json()
        return datos["rates"]["PEN"]
    except:
        return 3.39

def agregar_gasto(descripcion, monto, tipo_cambio):
    monto_usd = monto / tipo_cambio
    print(f"Gasto registrado: {descripcion}")
    print(f"S/. {monto:.2f} | ${monto_usd:.2f} USD")
    

def guardar_gasto(descripcion, monto):
    with open("gastos.csv", "a", newline="") as archivo:
        escribir = csv.writer(archivo)
        escribir.writerow([descripcion, monto])

def mostrar_gastos():
    print("\n" + "=" * 40)
    print("     REGISTRO DE GASTOS")
    print("=" * 40)
    with open("gastos.csv", "r") as archivo:
        leer = csv.reader(archivo)
        for fila in leer:
            print(f"{fila[0]:25} S/. {float(fila[1]):.2f}")
    print("=" * 40)

def calcular_resumen(tipo_cambio):
    montos = []
    with open("gastos.csv", "r") as archivo:
        leer = csv.reader(archivo)
        for fila in leer:
            montos.append(float(fila[1]))
    
    if not montos:
        print("No hay gastos registrados")
        return

    total = sum(montos)
    promedio = total / len(montos)

    print("\n" + "=" * 40)
    print("     RESUMEN")
    print("=" * 40)
    print(f"Total: S/. {total:.2f} | ${total / tipo_cambio:.2f} USD")
    print(f"Promedio: S/. {promedio:.2f}")
    print(f"Mayor: S/. {max(montos):.2f}")
    print(f"Menor: S/. {min(montos):.2f}")    
    print("=" * 40)


#PROGRAMA PRINCIPAL
tipo_cambio = obtener_tipo_cambio()

print("=" * 40)
print("     GESTOR DE GASTOS PERSONAL")
print(f"    Tipo de cambio: 1USD = S/. {tipo_cambio:.2f}")
print("=" * 40)

while True:
    print("\n1. Registrar gasto")
    print("2. Ver todos los gastos")
    print("3. Ver resumen")
    print("4. Salir")

    opcion = input("\nElige tu opción: ")

    if opcion == "1":
        descripcion = input("Descripcion: ")
        monto = float(input("Monto en soles: S/. "))
        agregar_gasto(descripcion, monto, tipo_cambio)
        guardar_gasto(descripcion, monto)
    
    elif opcion == "2":
        mostrar_gastos()
    
    elif opcion == "3":
        calcular_resumen(tipo_cambio)

    elif opcion == "4":
        print("Hasta pronto!")
        break
    
    else:
        print("Opción no válida. Elige entre 1 y 4")