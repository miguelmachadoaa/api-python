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

credentials_data = {
    "type": "service_account",
    "project_id": project_id,
    "private_key_id": private_key_id,
    "private_key": private_key,
    "client_email": client_email,
    "client_id": client_id,
    "auth_uri": auth_uri,
    "token_uri": token_uri,
    "auth_provider_x509_cert_url": auth_provider_x509_cert_url,
    "client_x509_cert_url": client_x509_cert_url,
    "universe_domain": universe_domain
}

credenciales = {
    "type": "service_account",
    "project_id": "api-5b334",
    "private_key_id": "05476dbc025529d916b7e904762e848ddb586a0b",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC5k/3AJpY57qMS\nmQ8Ol5BNn4YYg2XUv3IXVnsEdEydF962MCk0Kg+z9GuSp3zxMlnl3WCi88JD4//h\n3qEgtBsPjqZdC7StX+n6oBVKp0519ne1DhgGu1xFJJX2bgPOrnHieKdrlyG+YVbC\no0JrpBrKsDhYeO/STmvfBVTpGBsA5w68RKsjtYGG9qQRbT/OmituoeH0iUSo4UPB\nDXGudK+RcV9l5t0nZpZ0rG+WJcpud5DjDZFD2T7Gjt3aQXe4DiFTdVvdHj4Wl/3U\nU69pe1Ukt2+Z25bJgSxmhcgBnbDoMySmxonZuVEYJCuEVC2/wlvXpjmsUWzu9XhF\nxs2ffcXTAgMBAAECggEAHP/bKCg/fdJklEGWde10T3+irk5LiZPYdHzUoMJlvdS0\nPkccto9Da0Js1FAs+On+h1TxRsrjAXCYageRU/F2cGzBDYrd6IveSIZfMrkd9ywV\nJ8C0kMoS0KaMx/iyypzoT1S9tiqPS4Hy01vnbg0JDMG92awdryuxtU+kJaqufuos\n47FhNwk4l3ksdeiLwlV/Qso7SBtQ1fxhgQHweHc5EPnX/Tdj8XJvipRctALBdGDr\nrXl98ODxoO9u7uGZqRQxlSsnq2qSiIvHhXmGrnquRB/qJ+2r3VOr4YnhBInfp8Pg\nEsCMjpkEu20gpRHevMGAjFu/rlLTCz56DpFS/uquMQKBgQD9IB0yg3iZRdat0V89\nID9wsLz1iVDK0TNpVHdWMTfGq7k7K8xs6Qdb5XUajytTRFpQWn4F06A7WW4OmiGj\nh8mXIFQWL2kpZGojxn4DGK6FgtZMsZfcez3JEx0HoNAYfrDAGU8WUPMFX0MDCyzM\nEoY4wXhkZ+icXH6y+2cCNpsU8QKBgQC7r4Dq35QAoU2XecKvihTQcMHjYdpCSpGl\n+pAyM5VJUJFVlRRKEZe1yWQeti0V6OQ4PKxn7/PkVCRXdM4ULDBCSmAj0F9SL6C5\neORhSVq1qCYyTAUflw3VsNzlKdugXKfnsVwFjj4vttmVCg7LGEmdjAh+o0YDgIpc\nZJ2oIfj3AwKBgH+8JP/IuKMgSyWL8rO2Ak2r4q9FjC/NQlR0+4PTcoIfRmpFv/N1\n5PDK6j1s4kAyziCeidoG4WURzCgyP6d2bpSFC+nmIvtwYN+M2ypU2j0luV8af7gT\nuSovKwceb+TsieVm4DIyx3B+kiKHESQqdPFPMKH6jbfaNVW86E6Fn90BAoGAZTfx\nPrn1B6H2RorUA/dj4kXtSsOrAbVVdz36JhjLmg5pUs5jcs6qEs/ZvvZgukAvVGTk\nVemCjtESCFhmC1sJa7bQwn/N6HTnKR+Zix4UXYOhld6JpM/CFkyb1LsORx2xL7Lm\n/dgIkZL7JPWXpNAkY2Lx8dn8GEdqVwmsPNCVhCECgYA/hQmw1FprE00/HqZzljEV\nWM7ad9F70ew5F8MgS0fhIq0JbIXi3HDBUZW54rrF/URKZQGUZ/pen2jsrpq2kOsY\nEP1s/ksEniwHIQdd4ojo3XG37xHXisZfazoIrZStZSCx7kh5ds4BF6sngwpXl9j2\ncG2/ihH6A9UBkn4Qn6c+4w==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-fbsvc@api-5b334.iam.gserviceaccount.com",
    "client_id": "108862392730505847160",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40api-5b334.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

datos_json = json.dumps(credenciales)

cred = credentials.Certificate(credenciales) # Cambia por tu archivo JSON
firebase_admin.initialize_app(cred, {
    'databaseURL': database_url # Cambia por tu URL de Firebase
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
