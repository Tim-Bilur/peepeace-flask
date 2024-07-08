import RPi.GPIO as GPIO
import time
from firebase2 import get_relayph_from_firebase, update_relayph_in_firebase
from func_webcam import capture_image
from func_ph import read_ph
from func_motor_control import rotate_clockwise, rotate_counterclockwise, cleanup_gpio


# CHANGE THE LINK
FIREBASE_URL = "https://peeace-edf6e-default-rtdb.asia-southeast1.firebasedatabase.app/urine_reports.json"

# Run the main function
if __name__ == "__main__":
    try:
        while True:
            relayph_value = get_relayph_from_firebase(FIREBASE_URL)
            if relayph_value:

                #Menangkap Gambar
                capture_image()


                #Motor Stepper Memutar ke bawah
                steps_per_revolution = 2048  # Number of steps for 360 degrees rotation
                delay = 0.001  # Delay between steps

                # Rotate clockwise
                print("Rotating 360 degrees clockwise")
                rotate_clockwise(steps_per_revolution, delay)
               
                # Wait for 5 seconds
                print("Waiting for 5 seconds")
                time.sleep(3)

                #Sensor pH
                print("Memulai pembacaan sensor pH...")
                ph_value = read_ph()  # Default timeout is 10 seconds, can be adjusted if needed
                if ph_value is not None:
                    print(f"Nilai pH Terakhir: {ph_value:.2f}")
                else:
                    print("Gagal membaca nilai pH dalam batas waktu yang ditentukan...")
                
                #Motor Stepper Memutar ke atas
                print("Rotating 360 degrees counter-clockwise")
                rotate_counterclockwise(steps_per_revolution, delay)


                # Predik warna

                # Predik Penyakit

                # Nge False Firebase

                # Exit the program after one iteration

                print("=======================\nProgram Selesai")
                break
                
            else:
                print("=======================\nProgram Tidak Berjalan")
                # Exit the program if relayph_value is False

    finally:
        GPIO.cleanup()
