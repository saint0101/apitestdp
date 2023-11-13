

# liste contenant les données

# stores = {}
# items = {}
#
# _stores = {
#     "stores": [
#         {
#             "items": [
#                 {
#                     "name": "my item",
#                     "price": 15.99
#                 }
#             ],
#             "name": "My Store"
#         },
#         {
#             "items": [
#                 {
#                     "name": "tablette",
#                     "price": 2000
#                 },
#                 {
#                     "name": "tablette 2",
#                     "price": 3000
#                 },
#                 {
#                     "name": "tablette 2",
#                     "price": 3000
#                 }
#             ],
#             "name": "nouveau magasin 1"
#         }
#     ]
# # }


# configuration used to connect to MariaDB
# config = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'password': 'rootpassword',
#     'database': 'mydatabase'
# }

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myuser:mypassword@db/mydatabase'
db = SQLAlchemy(app)





import json

# import the necessary packages
import flask
import mariadb

from Api_rest.app.utils import test_db_connection
from .db import config

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# route to return all people
@app.route('/api/people', methods=['GET'])
def index():
   # connection for MariaDB
   conn = mariadb.connect(**config)
   # create a connection cursor
   cur = conn.cursor()
   # execute a SQL statement
   cur.execute("select * from people")

   # serialize results into JSON
   row_headers=[x[0] for x in cur.description]
   rv = cur.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))

   # return the results!
   return json.dumps(json_data)


@app.route('/test_db_connection')
def test_connection():
    if test_db_connection():
        return jsonify({'message': 'Database connection successful!'})
    else:
        return jsonify({'message': 'Database connection failed!'})
# app.run()
# app.run(debug=True, host='0.0.0.0')




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
#
if __name__ == '__main__':
    app.run(debug=True)
