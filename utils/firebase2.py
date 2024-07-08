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


def update_relay_from_firebase(url, new_relay_state):
    """
    Updates the 'relay' value in Firebase.

    Args:
    url (str): The URL to perform the PUT request.
    new_relay_state (dict): The new relay state to update.

    Returns:
    bool: True if the update is successful, False otherwise.
    """
    new_relay_state = False
    response = requests.put(url, json=new_relay_state)
    if response.status_code == 200:
        print("Relay state updated to false successfully.")
        return True
    else:
        print(
            f"Failed to update relay state in Firebase. HTTP Status code: {response.status_code}"
        )
        return False


def update_data_from_firebase(url, new_data):
    """
    Updates the 'data' value in Firebase.

    Args:
    url (str): The URL to perform the PUT request.
    new_data (dict): The new data to update.

    Returns:
    bool: True if the update is successful, False otherwise.
    """
    required_keys = ["color", "disease_indication", "image", "pH"]
    if all(key in new_data for key in required_keys):
        response = requests.put(url, json=new_data)
        if response.status_code == 200:
            print("Data updated successfully.")
            return True
        else:
            print(
                f"Failed to update data in Firebase. HTTP Status code: {response.status_code}"
            )
            return False
    else:
        print("Invalid data format.")
        return False
