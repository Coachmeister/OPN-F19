from flask import Flask, redirect, url_for, request, jsonify, Response
import mysql.connector


app = Flask(__name__)

@app.route('/person', methods = ['POST'])
def post():
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
def get():
	#return jsonify(PersonID = 0, firstname ="fuck", lastname = "you")
	cnx = mysql.connector.connect(user='root', password='',host='db',database='db')
	mycursor = cnx.cursor()
	sql = "SELECT * FROM persons"
	mycursor.execute(sql)
	cnx.commit()
	#return jsonify(data = mycursor.fetchall())
	#return Response(jsonify("personID","firstname","lastname"), 200)
	return jsonify(sql)
	mycursor.close()
	cnx.close()


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000, debug = True)
