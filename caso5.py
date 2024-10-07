import csv 
import json
from datetime import datetime

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
ultima_posicion_por_matricula = {}

#Ordenamos por matrícula y luego por fecha
data_ordenada = sorted(data, key=lambda x: (x['Matricula'], -int(x['Pos_date'])))

#Iteramos sobre los datos agrupados por matrícula
for i in range(1, len(data_ordenada)):
    matricula_actual = data_ordenada[i]['Matricula']
    if matricula_actual not in ultima_posicion_por_matricula:
        #Convertimos de milisegundos a segundos dividiendo entre 1000
        fecha_segundos = float(data_ordenada[i]['Pos_date']) / 1000
        #Convertimos a formato de fecha y hora
        fecha_formateada = datetime.utcfromtimestamp(fecha_segundos).strftime('%d/%m/%Y %H:%M:%S')
        matricula=data_ordenada[i]['Matricula']
        ultima_posicion_por_matricula[matricula] = fecha_formateada

datos_ordenados = sorted(ultima_posicion_por_matricula.items(), key=lambda x: datetime.strptime(x[1], "%d/%m/%Y %H:%M:%S"), reverse=True)


#Creamos la estructura de datos en formato JSON
resultado_json = [
        {
            "matricula": matricula,
            "ultima_fecha_registrada": fecha_formateada
        }
        for matricula, fecha_formateada in datos_ordenados
    ]


#Escribimos los resultados en un archivo JSON
with open("resultados_ultima_posicion.json", "w") as archivo:
    json.dump(resultado_json, archivo, indent=4)

#Escribimos los mismos resultados en un archivo CSV
with open("resultados_ultima_posicion.csv", "w", newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=["matricula", "ultima_fecha_registrada"])
    escritor_csv.writeheader()  #Encabezados
    escritor_csv.writerows(resultado_json)  #Filas con los datos

print(f" {len(datos_ordenados)} vehiculos han sido almacenados en el fichero 'resultados_ultima_posicion.json' ")