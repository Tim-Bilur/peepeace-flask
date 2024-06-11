import firebase_admin
from firebase_admin import credentials, db

# Define the credentials path and database URL as constants
CREDENTIALS_PATH = "./credentials/firebase_credentials.json"
DATABASE_URL = "https://peepeace-app-default-rtdb.asia-southeast1.firebasedatabase.app/"


def initialize_firebase_and_update_relayph(relayph_value):
    """
    Initializes Firebase, retrieves the 'relayPH' field, updates it, and returns the updated value.

    Args:
    relayph_value (bool): The value to update the 'relayPH' field to.

    Returns:
    bool: The updated 'relayPH' value.
    """
    # Initialize the app with a service account, granting admin privileges
    cred = credentials.Certificate(CREDENTIALS_PATH)
    firebase_admin.initialize_app(
        cred,
        {"databaseURL": DATABASE_URL},
    )

    # Reference to the 'relayPH' field
    relayph_ref = db.reference("urine_reports/relayPH")

    # Perform GET request to retrieve the current 'relayPH' value
    current_relayph = relayph_ref.get()
    print("Current relayPH value from Firebase:", current_relayph)

    # Update the 'relayPH' field
    relayph_ref.set(relayph_value)

    # Verify the update by getting the updated value
    updated_relayph = relayph_ref.get()
    print("Updated relayPH value from Firebase:", updated_relayph)

    return updated_relayph


# # Example usage
# relayph_value = False

# updated_relayph = initialize_firebase_and_update_relayph(relayph_value)
# print("Final updated relayPH value:", updated_relayph)
