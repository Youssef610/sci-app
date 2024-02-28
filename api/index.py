from flask import Flask, request, jsonify
from login import loginPage
app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Server For Our SCI APP...</h1>'


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        id = data['id']
        code = data['code']
        extracted_data = loginPage(id, code)
    except Exception as e:
        error_message = "Internal Server Error: {}".format(str(e))
        return jsonify({"error": error_message}), 500

    return jsonify(extracted_data)
