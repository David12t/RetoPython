from flask import Flask, jsonify, request
import json

app = Flask(__name__)

#Función para leer los datos almacenados en un archivo JSON
def leer_datos_json():
    with open("resultados_ultima_posicion.json", "r") as archivo:
        datos = json.load(archivo)
    return datos

#Ruta para obtener la última fecha de una matrícula
@app.route('/<matricula>', methods=['GET'])
def obtener_fecha_matricula(matricula):
    #Leemos los datos del archivo JSON
    datos = leer_datos_json()
    
    #Buscamos la matrícula
    for vehiculo in datos["vehiculos"]:
        if vehiculo["matricula"] == matricula:
            return jsonify({
                "matricula": matricula,
                "ultima_fecha_registrada": vehiculo["ultima_fecha_registrada"]
            }), 200
    
    #Si la matrícula no se encuentra, devolvemos un mensaje de error
    return jsonify({"error": "Matricula no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
