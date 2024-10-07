import csv
import json

nombre_archivo = 'reto.csv'

#Lista donde almacenaremos los datos del CSV
datos_csv = []

#Abrimos el archivo CSV y leerlo
with open(nombre_archivo, mode='r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)  #Usamos DictReader para que cada fila sea un diccionario
    for fila in lector_csv:
        datos_csv.append(fila)

#Convertimos una objeto python en una cadena de texto en JSON
datos_json = json.dumps(datos_csv, indent=4)
#Convierte una cadena de JSON a un objeto de python (lista de diccionarios)
datos = json.loads(datos_json)

#Diccionario para almacenar el sumatorio de distancias por matrícula
distancias_por_matricula = {}

#Recorremos los datos y calculamos el sumatorio por matrícula
for item in datos:
    matricula = item['Matricula']
    
    distancia = float(item['Distance'])
    
    #Sumamos la distancia a la matrícula correspondiente
    if matricula in distancias_por_matricula:
        distancias_por_matricula[matricula] += distancia
    else:
        distancias_por_matricula[matricula] = distancia

#Finalmente imprimimos el sumatorio de distancias para cada matrícula
for matricula, sumatorio in distancias_por_matricula.items():
    print(f"El vehiculo con matrícula: {matricula} ha recorrido la siguiente distancia: {sumatorio}")

