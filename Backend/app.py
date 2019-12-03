from flask import Flask, redirect url_for, request
app = Flask(__name__)

@app.route('/insert', methods = ['POST'])
def set_persons():
	if request.method == 'POST':
	return jsonify({'persons': persons})


