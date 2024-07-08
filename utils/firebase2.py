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
