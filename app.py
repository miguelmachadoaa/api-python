from flask import Flask, jsonify, request
import mysql.connector 
import firebase_admin 
from firebase_admin import credentials, db

app = Flask(__name__)

cred = credentials.Certificate("presupuesto-d827e-firebase-adminsdk-nwxyl-0ee0565833.json") # Cambia por tu archivo JSON
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://api-5b334-default-rtdb.firebaseio.com/' # Cambia por tu URL de Firebase
})

@app.route('/')
def index():
    params = request.args
    id = params.get('id') 
    itemId = params.get('itemId') 

    if id:
        if itemId:
            ref = db.reference('{id}/{itemId}'.format(id=id, itemId=itemId))
            datos = ref.get()
            return jsonify(datos)
        else:
            #buscar todos los videos
            ref = db.reference(id)
            datos = ref.get()
            return jsonify(datos)
    else:
        return jsonify({"mensaje": "No se han enviado datos"})


@app.route('/', methods=['POST'])
def insertar():
    params = request.args
    id = params.get('id') 

    if not id:
        return jsonify({"mensaje": "No se ha enviado el ID"})
    
    ref = db.reference(id)
    data = request.json
    ref.push(data)
    return jsonify({"mensaje": "Datos insertados correctamente"})

if __name__ == '__main__':
    app.run(debug=True)
