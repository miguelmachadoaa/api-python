from flask import Flask, jsonify, request
import mysql.connector 

app = Flask(__name__)

# Configuración de la conexión a MySQL
db_config = {
    'host': '144.217.200.63',        # Cambia a tu servidor MySQL
    'user': 'maymicov_agencia',       # Usuario de MySQL
    'password': '2MkPvV6n',# Contraseña de MySQL
    'database': 'maymicov_agenciamaymi' # Nombre de la base de datos
}

@app.route('/')
def index():
    return "API para MySQL"


# Ruta para obtener datos de MySQL
@app.route('/data', methods=['GET'])
def get_data():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")  # Ajusta según tu tabla
        rows = cursor.fetchall()
        return jsonify(rows)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)})
    finally:
        cursor.close()
        conn.close()

# Ruta para insertar datos en MySQL
@app.route('/data', methods=['POST'])
def insert_data():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        data = request.json
        query = "INSERT INTO users (columna1, columna2) VALUES (%s, %s)"
        values = (data['columna1'], data['columna2'])
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"mensaje": "Datos insertados correctamente"})
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)})
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
