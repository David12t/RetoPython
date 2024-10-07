import csv
import json


nombre_archivo = 'reto.csv'

#Lista donde almacenaremos los datos del CSV en JSON
datos_csv = []

# Abrir el archivo CSV y leerlo
with open(nombre_archivo, mode='r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)  # Usamos DictReader para que cada fila sea un diccionario
    for fila in lector_csv:#Recorremos cada fila y lo añadimos a la lista
        datos_csv.append(fila)

#Convertimos la lista a formato JSON
datos_json = json.dumps(datos_csv, indent=4)

#Imprimimos los datos en formato JSON
print(datos_json)
