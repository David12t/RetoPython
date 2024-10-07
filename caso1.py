import csv

#Nombre del archivo CSV
nombre_archivo = 'reto.csv'

#Abrir el archivo CSV en modo lectura y leerlo
with open(nombre_archivo, mode='r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    
    #Recorre cada linea y la imprime
    for linea in lector_csv:
        print(linea)
