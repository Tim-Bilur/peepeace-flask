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


@app.route("/data", methods=["GET", "PUT"])
def firebase_data():
    if request.method == "GET":
        response = requests.get(url_update_data)
        data = response.json()
        print(data)
        return jsonify(data)
    elif request.method == "PUT":
        new_data = request.json
        if all(
            key in new_data for key in ["color", "disease_indication", "image", "pH"]
        ):
            response = requests.put(url_update_data, json=new_data)
            if response.status_code == 200:
                return jsonify({"message": "Data updated successfully"}), 200
            else:
                return (
                    jsonify({"message": "Failed to update data"}),
                    response.status_code,
                )
        else:
            return jsonify({"message": "Invalid data format"}), 400


@app.route("/relay", methods=["GET", "PUT"])
def firebase_relay():
    if request.method == "GET":
        response = requests.get(url_update_relay)
        data = response.json()
        print(data)
        return jsonify(data)
    elif request.method == "PUT":
        # Change relay state to false without requiring input data
        new_relay_state = False
        response = requests.put(url_update_relay, json=new_relay_state)
        if response.status_code == 200:
            return (
                jsonify({"message": "Relay state updated to false successfully"}),
                200,
            )
        else:
            return (
                jsonify({"message": "Failed to update relay state"}),
                response.status_code,
            )


if __name__ == "__main__":
    app.run(debug=True)
