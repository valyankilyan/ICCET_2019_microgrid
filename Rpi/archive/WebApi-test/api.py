from flask import Flask, escape, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return "Hello, {}!".format(escape(name))

@app.route('/post', methods=['POST'])
def api_all():
    return jsonify("jsonify")

@app.route('/get', methods=['GET'])
def api_all():
    return jsonify("jsonify")



if __name__ == '__main__':
	app.run(debug=True, port=5000)