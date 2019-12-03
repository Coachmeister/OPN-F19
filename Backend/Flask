from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)


@app.route('/person', methods = ['POST'])
def post():
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	submit = request.form['submit']

@app.route('/person', methods = ['GET'])
def get():
	return jsonify(PersonID = 0, firstname ="fuck", lastname = "you")


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000, debug = True)
