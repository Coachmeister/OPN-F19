from flask import Flask, redirect, url_for, request, jsonify
from mysql.connector import (connection)
app = Flask(__name__)

cnx = connection.MySQLConnection(user='Jonas', password='password',
                                 host='localhost',
								database='people')
cnx.close()


@app.route('/person/', methods = ['POST'])
def post():
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	submit = request.form['submit']

@app.route('/persons/', methods = ['GET'])
def get():
	return jsonify(PersonID = 0, firstname ="fuck", lastname = "you")


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000, debug = True)
