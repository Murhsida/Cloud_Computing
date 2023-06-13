from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Connect to the MySQL database
    cnx = mysql.connector.connect(
        user='YOUR_MYSQL_USERNAME',
        password='YOUR_MYSQL_PASSWORD',
        host='YOUR_MYSQL_INSTANCE_CONNECTION_NAME',
        database='YOUR_MYSQL_DATABASE_NAME',
        unix_socket='/cloudsql/YOUR_MYSQL_INSTANCE_CONNECTION_NAME'
    )

    cursor = cnx.cursor()

    # Check if the user exists and the password is correct
    query = 'SELECT * FROM users WHERE username = %s AND password = %s'
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        return 'Login successful'
    else:
        return 'Invalid credentials'

    cursor.close()
    cnx.close()

if __name__ == '__main__':
    app.run()
