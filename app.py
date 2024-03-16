from flask import Flask, request, jsonify
from login import loginPage
from natiga import get_natiga
from register import get_register

app = Flask(__name__)


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


@app.route('/natiga', methods=['POST'])
def natiga():
    try:
        data = request.get_json()
        ID = data['id']
        code = data['code']
        extracted_data = get_natiga(ID, code)
    except Exception as e:
        error_message = "Internal Server Error: {}".format(str(e))
        return jsonify({"error": error_message}), 500

    return extracted_data


@app.route('/register', methods=['POST'])
def register():
    try:
        print('WE IN REGISTER')
        data = request.get_json()
        ID = data['id']
        code = data['code']
        extracted_data = get_register(ID, code)
    except Exception as e:
        error_message = "Internal Server Error: {}".format(str(e))
        return jsonify({"error": error_message}), 500
    return extracted_data


@app.route('/')
def home():
    return jsonify({"msg": "Server For Our SCI APP..."})
