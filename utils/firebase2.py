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
            print("Failed to retrieve 'relayPH' value from Firebase.")
            return None
    else:
        print(
            f"Failed to retrieve data from Firebase. HTTP Status code: {response.status_code}"
        )
        return None


def update_relayph_in_firebase(url, new_relayph):
    """
    Updates the 'relayPH' value in Firebase.

    Args:
    url (str): The URL to perform the PUT request.
    new_relayph (bool): The new value for 'relayPH'.

    Returns:
    bool: True if the update was successful, False otherwise.
    """
    updated_data = {"relay": new_relayph}
    response = requests.put(url, json=updated_data)
    if response.status_code == 200:
        print("RelayPH value updated successfully.")
        return True
    else:
        print(
            f"Failed to update RelayPH value in Firebase. HTTP Status code: {response.status_code}"
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
