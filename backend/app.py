from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# Configure MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',  # or your MySQL server
        user='root',       # your MySQL username
        password='password', # your MySQL password
        database='mydatabase' # your MySQL database name
    )

# API Endpoint Example
# @app.route('/api/data')
# def get_data():
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
#     cursor.execute('SELECT * FROM my_table')  # Your MySQL query
#     rows = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)
