# This Flask APP Server

from flask import Flask, jsonify, request
import requests
from utils.firebase2 import update_firebase_data

# Define the URL for the GET request
url = "https://peepeace-app-default-rtdb.asia-southeast1.firebasedatabase.app/urine_reports.json"

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"Message": "Hello FLASK"})


@app.route("/firebase", methods=["GET"])
def firebase_response():
    response = requests.get(url)
    data = response.json()
    return jsonify({"status": 200, "message": data})


@app.route("/firebase", methods=["PUT"])
def update_firebase():
    data = request.json
    if data:
        response, status_code = update_firebase_data(url, data)  # Fix the function call
        return jsonify(response), status_code
    else:
        return jsonify({"error": "No data provided for update."}), 400


if __name__ == "__main__":
    app.run(debug=True)
