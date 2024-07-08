from flask import Flask, jsonify, request
import requests
from utils.config import get_firebase

# Define the URL for the GET request
url = get_firebase()

url_index = f"{url}.json"
url_update_data = f"{url}/data.json"
url_update_relay = f"{url}/relay.json"

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"Message": "Hello FLASK"})


@app.route("/firebase", methods=["GET"])
def firebase_response():
    response = requests.get(url_index)
    data = response.json()
    print(data)
    return jsonify(data)


@app.route("/data", methods=["GET"])
def firebase_data():
    response = requests.get(url_update_data)
    data = response.json()
    print(data)
    return jsonify(data)


@app.route("/data", methods=["PUT"])
def update_data():
    response = requests.get(url_update_data)
    data = response.json()
    print(data)
    return jsonify(data)


@app.route("/relay", methods=["GET"])
def firebase_relay():
    response = requests.get(url_update_relay)
    data = response.json()
    print(data)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
