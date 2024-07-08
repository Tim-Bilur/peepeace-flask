import requests


def get_relayph_from_firebase(url):
    """
    Retrieves the 'relayPH' value from Firebase.

    Args:
    url (str): The URL to perform the GET request.

    Returns:
    bool: The 'relayPH' value retrieved from Firebase, or None if the request fails.
    """
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        relayph_value = data.get("relay")
        if relayph_value is not None:
            return relayph_value
        else:
            print("Failed to retrieve 'relay' value from Firebase.")
            return None
    else:
        print(
            f"Failed to retrieve data from Firebase. HTTP Status code: {response.status_code}"
        )
        return None


def update_relayph_in_firebase(url, new_relayph):
    """
    Updates the 'relay' value in Firebase.

    Args:
    url (str): The URL to perform the PUT request.
    new_relayph (bool): The new value for 'relay'.

    Returns:
    bool: True if the update was successful, False otherwise.
    """
    updated_data = {"relay": new_relayph}
    response = requests.put(url, json=updated_data)
    if response.status_code == 200:
        print("Relay value updated successfully.")
        return True
    else:
        print(
            f"Failed to update Relay value in Firebase. HTTP Status code: {response.status_code}"
        )
        return False


def update_firebase_data(url, data):
    """
    Update data in Firebase Realtime Database.

    Args:
    url (str): The URL to perform the PUT request.
    data (dict): Dictionary containing fields to update.

    Returns:
    tuple: A tuple containing the JSON response from the Firebase API and the HTTP status code.
    """
    response = requests.put(url, json=data)
    return response.json(), response.status_code


def update_data(url, updated_data):
    existing_data = requests.get(url).json().get("data", {})
    updated_data_merged = {"data": {**existing_data, **updated_data}}
    response = requests.put(url, json=updated_data_merged)
    if response.status_code == 200:
        print("Data updated successfully.")
        return True
    else:
        print(
            f"Failed to update data in Firebase. HTTP Status code: {response.status_code}"
        )
        return False


def update_relay(url, new_relay):
    updated_data = {"relay": new_relay}
    response = requests.put(url, json=updated_data)
    if response.status_code == 200:
        print("Relay value updated successfully.")
        return True
    else:
        print(
            f"Failed to update relay value in Firebase. HTTP Status code: {response.status_code}"
        )
        return False


def store_data(url, data):
    if "relay" in data:
        return update_relay(url, data["relay"])
    elif "data" in data:
        return update_data(url, data["data"])
    else:
        print("Invalid data format.")
        return False
