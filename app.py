# This Flask APP Server

from flask import Flask, jsonify, request
import requests
from utils.firebase2 import update_firebase_data, update_relayph_in_firebase
from utils.firebase2 import update_data, update_relay, store_data
from utils.config import get_firebase

# Define the URL for the GET request
url = get_firebase()

url_index = f"{url}.json"
url_update_data = f"{url}/data"
url_update_relay = f"{url}/relay"

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"Message": "Hello FLASK"})


@app.route("/firebase", methods=["GET"])
def firebase_response():
    response = requests.get(url_index)
    data = response.json()
    return jsonify(data)


@app.route("/firebase", methods=["PUT"])
def update_data():
    data = request.json
    if data:
        response, status_code = update_firebase_data(url, data)  # Fix the function call
        return jsonify(response), status_code
    else:
        return jsonify({"error": "No data provided for update."}), 400


@app.route("/ph", methods=["PUT"])
def update_relay():
    data = request.json
    if data and "relay" in data:
        relay = data["relay"]
        response_status = update_relayph_in_firebase(url, relay)
        if response_status:
            return jsonify({"message": "Relay value updated successfully."}), 200
        else:
            return jsonify({"error": "Failed to update Relay value in Firebase."}), 500
    else:
        return jsonify({"error": "Invalid data format or 'relay' field missing."}), 400


@app.route("/update_data", methods=["PUT"])
def update_data_route():
    data = request.json
    if data:
        response, status_code = update_firebase_data(url_update_data, data)
        return jsonify(response), status_code
    else:
        return jsonify({"error": "No data provided for update."}), 400


@app.route("/update_relay", methods=["PUT"])
def update_relay_route():
    data = request.json
    if data and "relay" in data:
        response_status = store_data(url_update_relay, data)
        if response_status:
            return jsonify({"message": "Relay value updated successfully."}), 200
        else:
            return jsonify({"error": "Failed to update relay value in Firebase."}), 500
    else:
        return jsonify({"error": "Invalid data format or 'relay' field missing."}), 400


if __name__ == "__main__":
    app.run(debug=True)
