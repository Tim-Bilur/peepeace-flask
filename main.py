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
from utils.firebase2 import get_relayph_from_firebase, update_relayph_in_firebase
import time
import RPi.GPIO as GPIO

if __name__ == "__main__":
    try:
        while True:
            relayph_value = get_relayph_from_firebase()
            if relayph_value:
                # Menangkap Gambar
                capture_image()

                # Motor Stepper Memutar ke bawah
                steps_per_revolution = 2048  # Number of steps for 360 degrees rotation
                delay = 0.001  # Delay between steps

                # Rotate clockwise
                print("Rotating 360 degrees clockwise")
                rotate_clockwise(steps_per_revolution, delay)

                # Wait for 5 seconds
                print("Waiting for 5 seconds")
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
                rotate_counterclockwise(steps_per_revolution, delay)

                # Predik warna
                image_path = "tmp/captured_image.jpg"

                # Extract RGB values from the image
                rgb_value = extract_rgb_from_image(image_path)

                # Predik Penyakit
                result = predict_disease_from_urine(rgb_value, ph_value)

                # Upload imgkit
                upload_result = upload_image(image_path)
                if upload_result:
                    print("Upload result:", upload_result)

                print(result)

                # Nge False Firebase

                # Exit the program after one iteration

                print("=======================\nProgram Selesai")
                break
            else:
                print("=======================\nProgram Tidak Berjalan")

    finally:
        GPIO.cleanup()
