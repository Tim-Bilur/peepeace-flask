# This Flask APP Server

from flask import Flask, jsonify, request
import requests

# Define the URL for the GET request
url = "https://peepeace-app-default-rtdb.asia-southeast1.firebasedatabase.app/urine_reports.json"


def update_firebase_data(data):
    """
    Update data in Firebase Realtime Database.

    Args:
    data (dict): Dictionary containing fields to update.

    Returns:
    dict: JSON response from the Firebase API.
    """
    response = requests.put(url, json=data)
    return response.json(), response.status_code


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
        response, status_code = update_firebase_data(data)
        return jsonify(response), status_code
    else:
        return jsonify({"error": "No data provided for update."}), 400


if __name__ == "__main__":
    app.run(debug=True)
