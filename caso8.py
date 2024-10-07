from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

#Configuramos la conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["miBaseDeDatos"]
collection = db["miColeccion"]


#Definir una ruta para obtener un dato por matrícula
@app.route("/api/datos/<string:matricula>", methods=["GET"])
def obtener_dato_por_matricula(matricula):
    #Buscar un registro por matrícula proporcionada en la URL
    dato = collection.find_one({"matricula": matricula}, {"_id": 0})
    if dato:
        return jsonify(dato['ultima_fecha_registrada'])
    else:
        return jsonify({"error": "No se encontró la matrícula solicitada"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
