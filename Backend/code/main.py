from flask import Flask, redirect, url_for, request, jsonify, Response
from flask_cors import CORS, cross_origin
import mysql.connector
import json


app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/person', methods = ['POST'])
@cross_origin(supports_credentials=True)
def post():
	#return jsonify("ddddd")
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	cnx = mysql.connector.connect(user='root', password='',host='db',database='db')
	mycursor = cnx.cursor()
	sql = "INSERT INTO persons(firstname, lastname) VALUES (%s,%s)"
	mycursor.execute(sql,(firstname, lastname))
	cnx.commit()
	return Response('', 200)
	mycursor.close()
	cnx.close()

@app.route('/persons/', methods = ['GET'])
@cross_origin(supports_credentials=True)
def get():
	
	cnx = mysql.connector.connect(user='root', password='',host='db',database='db')
	cursor = cnx.cursor()
	cursor.execute('SELECT * FROM persons')
	row_headers=[x[0] for x in cursor.description]
	rv = cursor.fetchall()
	json_data=[]
	for result in rv:
		json_data.append(dict(zip(row_headers,result)))
	return json.dumps(json_data, 200)
	#return jsonify(("PersonID","Firstname","Lastname"), 200)
	#return Response(jsonify(results))
	cursor.close()
	cnx.close()


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000, debug = True)
