from utils.func_colorPrediction import extract_rgb_from_image
from utils.func_disease import predict_disease_from_urine
from utils.func_imgkit import upload_image
from utils.func_webcam import capture_image
from utils.func_ph import read_ph
from utils.func_motor_control import (
    rotate_clockwise,
    rotate_counterclockwise,
    cleanup_gpio,
)
from utils.firebase2 import get_relayph_from_firebase
import RPi.GPIO as GPIO
from utils.config import get_firebase
import time
import requests

url = get_firebase()

url_index = f"{url}.json"
url_update_data = f"{url}/data.json"
url_update_relay = f"{url}/relay"


def update_relay_state():
    url = "http://127.0.0.1:5000/relay"  # Replace with your Flask server's IP and port
    response = requests.put(url)

    if response.status_code == 200:
        print("Relay state updated to false successfully.")
        print(response.json())
    else:
        print(f"Failed to update relay state. Status code: {response.status_code}")
        print(response.json())


# def update_data():
#     url = "http://127.0.0.1:5000/data"  # Replace with your Flask server's IP and port
#     new_data = {
#         "color": "yellow",
#         "disease_indication": "none",
#         "image": "path/to/image.jpg",
#         "pH": 7,
#     }
#     response = requests.put(url, json=new_data)

#     if response.status_code == 200:
#         print("Data updated successfully.")
#         print(response.json())
#     else:
#         print(f"Failed to update data. Status code: {response.status_code}")
#         print(response.json())


if __name__ == "__main__":
    try:
        while True:
            relayph_value = get_relayph_from_firebase(url_index)
            if relayph_value:
                # Menangkap Gambar
                print("Capture Image")
                capture_image()

                # Motor Stepper Memutar ke bawah
                steps_per_revolution = 2048  # Number of steps for 360 degrees rotation
                delay = 0.001  # Delay between steps

                # Rotate clockwise
                print("Rotating 360 degrees clockwise")
                # rotate_clockwise(steps_per_revolution, delay)

                # Wait for 5 seconds
                print("Waiting for 3 seconds for pH")
                time.sleep(3)

                # Sensor pH
                print("Memulai pembacaan sensor pH...")
                ph_value = (
                    read_ph()
                )  # Default timeout is 10 seconds, can be adjusted if needed
                if ph_value is not None:
                    print(f"Nilai pH Terakhir: {ph_value:.2f}")
                else:
                    print("Gagal membaca nilai pH dalam batas waktu yang ditentukan...")

                # Motor Stepper Memutar ke atas
                print("Rotating 360 degrees counter-clockwise")
                # rotate_counterclockwise(steps_per_revolution, delay)

                # Predik warna
                image_path = "tmp/captured_image.jpg"

                # Extract RGB values from the image
                rgb_value = extract_rgb_from_image(image_path)

                # Predik Penyakit
                result = predict_disease_from_urine(rgb_value, ph_value)

                # Upload imgkit
                upload_result, random_file_name = upload_image(image_path)
                if upload_result:
                    print("Upload result:", upload_result)

                print(result)

                # PUT the data
                url = "http://127.0.0.1:5000/data"

                new_data = {
                    "color": result['name_color'],
                    "disease_indication": result['disease'],
                    "image": f"https://ik.imagekit.io/peeace/{random_file_name}",
                    "pH": f"{ph_value:.2f}"
                }

                print(new_data)

                response = requests.put(url, json=new_data)

                if response.status_code == 200:
                    print("Data updated successfully.")
                    print(response.json())
                else:
                    print(f"Failed to update data. Status code: {response.status_code}")
                    print(response.json())


                # Nge False Firebase
                update_relay_state()

                # Exit the program after one iteration

                print("=======================\nProgram Selesai")
                
            else:
                print("=======================\nProgram Tidak Berjalan")

    finally:
        GPIO.cleanup()
