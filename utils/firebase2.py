import requests

# Define the URL for the GET request
url = "https://peepeace-app-default-rtdb.asia-southeast1.firebasedatabase.app/urine_reports.json"

# Perform the GET request to retrieve the current data
response_before = requests.get(url)
data_before = response_before.json()
print("Data before update:", data_before)

# Define the URL for the PUT request
url = "https://peepeace-app-default-rtdb.asia-southeast1.firebasedatabase.app/urine_reports.json"

# Data to be updated
updated_data = {"relayPH": True}

# Perform the PUT request without authentication
response = requests.put(url, json=updated_data)

# Check if the request was successful
if response.status_code == 200:
    print("Data updated successfully.")
else:
    print(f"Failed to update data. HTTP Status code: {response.status_code}")

# Perform another GET request to retrieve the updated data
response_after = requests.get(url)
data_after = response_after.json()
print("Data after update:", data_after)
