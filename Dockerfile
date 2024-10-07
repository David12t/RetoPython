FROM mongo:latest

COPY resultados_ultima_posicion.json /resultados_ultima_posicion.json

CMD mongoimport --host localhost --db mibasededatos --collection resultados --type json --file /resultados_ultima_posicion.json --jsonArray && mongod