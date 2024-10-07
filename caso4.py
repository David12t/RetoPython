import csv
import json
import math

def haversine(lat1, lon1, lat2, lon2):
    # Radio de la Tierra en kilómetros
    R = 6371.0

    # Convertir grados a radianes
    lat1 = math.radians(float(lat1))
    lon1 = math.radians(float(lon1))
    lat2 = math.radians(float(lat2))
    lon2 = math.radians(float(lon2))

    # Diferencia entre latitudes y longitudes
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula de Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distancia
    distance = R * c
    return distance


    
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
data = json.loads(datos_json)

#Diccionario para almacenar las distancias por matrícula
distancias_por_matricula = {}

#Ordenar por matrícula y luego por fecha
data_ordenada = sorted(data, key=lambda x: (x['Matricula'], x['Pos_date']))

#Iterar sobre los datos agrupados por matrícula
for i in range(1, len(data_ordenada)):
    matricula_actual = data_ordenada[i]['Matricula']
    matricula_anterior = data_ordenada[i-1]['Matricula']
    
    #Solo calcular la distancia si es la misma matrícula
    if matricula_actual == matricula_anterior:
        lat1 = data_ordenada[i-1]['Latitud']
        lon1 = data_ordenada[i-1]['Longitud']
        lat2 = data_ordenada[i]['Latitud']
        lon2 = data_ordenada[i]['Longitud']
        
        #Calcular distancia usando Haversine
        distancia = haversine(lat1, lon1, lat2, lon2)
        
        #Sumar la distancia al sumatorio de la matrícula
        if matricula_actual in distancias_por_matricula:
            distancias_por_matricula[matricula_actual] += distancia
        else:
            distancias_por_matricula[matricula_actual] = distancia

#Imprimir los resultados por matrícula
for matricula, distancia_total in distancias_por_matricula.items():
    print(f"Matrícula: {matricula}, Distancia total: {distancia_total:.2f} km")





