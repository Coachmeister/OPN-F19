from flask import Flask, redirect, url_for, request, jsonify, Response
import mysql.connector


app = Flask(__name__)

@app.route('/person', methods = ['POST'])
def post():
	Firstname = request.form['Firstname']
	Lastname = request.form['Lastname']
	cnx = mysql.connector.connect(user='root', password='',host='db',database='db')
	mycursor = cnx.cursor()
	sql = "INSERT INTO persons(Firstname, Lastname) VALUES (%s,%s)"
	mycursor.execute(sql,(Firstname, Lastname))
	cnx.commit()
	return Response('', 200)
	mycursor.close()
	cnx.close()

@app.route('/persons/', methods = ['GET'])
def get():
	return jsonify(PersonID = 0, firstname ="fuck", lastname = "you")
	cnx = mysql.connector.connect(user='root', password='',host='db',database='db')



if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000, debug = True)
