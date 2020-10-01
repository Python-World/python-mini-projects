from flask import Flask , jsonify
import requests
import json
app = Flask(__name__)
#GET ALL API DATA
#http://127.0.0.1:8000/
@app.route('/')
def get_api():
	r = requests.get('https://jsonplaceholder.typicode.com/todos/')
	data = json.dumps(r.json())
	return jsonify (json.loads(data))
#GET API BY Id
#http://127.0.0.1:8000/1
@app.route('/<id>')
def get_api_by_id(id):
	r = requests.get('https://jsonplaceholder.typicode.com/todos/'+str(id))
	data = json.dumps(r.json())
	return jsonify (json.loads(data))

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8000)