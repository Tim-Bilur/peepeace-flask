import firebase_admin
from firebase_admin import credentials, db
import os

# Set the path to your credentials file relative to main.py
CREDENTIALS_PATH = os.path.join("utils", "credentials", "firebase_credentials.json")

# Initialize Firebase Admin SDK
def initialize_firebase():
    try:
        cred = credentials.Certificate(CREDENTIALS_PATH)  # Path to your credentials
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://peeace-edf6e-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Your Firebase database URL
        })
        print("Firebase initialized successfully.")
    except Exception as e:
        print(f"Error initializing Firebase: {e}")

# Function to retrieve data from Firebase Realtime Database
def retrieve_data(reference_path):
    try:
        ref = db.reference(reference_path)  # Reference to the specific path in your database
        data = ref.get()  # Fetch data from Firebase
        if data:
            print("Data retrieved successfully:")
            print(data)
        else:
            print("No data found at the specified path.")
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Main function
if __name__ == "__main__":
    initialize_firebase()
    reference_path = "urine_reports"  # Path to the data in your database
    retrieved_data = retrieve_data(reference_path)
