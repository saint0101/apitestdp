from flask import Flask, jsonify
import pymysql.cursors

app = Flask(__name__)

def te_db_connection():
    connection = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='rootpassword',
        database='mydatabase',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # Execute a simple query to test the connection
            cursor.execute('SELECT 1')
            result = cursor.fetchone()

            if result:
                return True
            else:
                return False
    finally:
        connection.close()

@app.route('/test_db_connection')
def test_connection():
    if te_db_connection():
        return jsonify({'message': 'Database connection successful!'})
    else:
        return jsonify({'message': 'Database connection failed!'})

if __name__ == '__main__':
    app.run(debug=True)