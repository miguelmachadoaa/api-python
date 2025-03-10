from flask import Flask, jsonify, request
import mysql.connector 
import firebase_admin 
from firebase_admin import credentials, db
from dotenv import load_dotenv
import os
import json

app = Flask(__name__)

load_dotenv()

type = os.getenv("TYPE")
project_id = os.getenv("PROJECT_ID")
private_key_id = os.getenv("PRIVATE_KEY_ID")
private_key = os.getenv("PRIVATE_KEY")
client_email = os.getenv("CLIENT_EMAIL")
client_id = os.getenv("CLIENT_ID")
auth_uri = os.getenv("AUTH-URI")
token_uri = os.getenv("TOKEN_URI")
auth_provider_x509_cert_url = os.getenv("AUTH_PROVIDER_X509_CERT_URL")
client_x509_cert_url = os.getenv("CLIENT_X509_CERT_URL")
universe_domain = os.getenv("UNIVERSE_DOMAIN")
database_url = os.getenv("DATABASE_URL")

cred = credentials.Certificate('presupuesto-d827e-firebase-adminsdk-nwxyl-0ee0565833.json') # Cambia por tu archivo JSON
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://api-5b334-default-rtdb.firebaseio.com" # Cambia por tu URL de Firebase
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
