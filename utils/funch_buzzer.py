import RPi.GPIO as GPIO
import time

# Konfigurasi pin
BUZZER_PIN = 16  # Sesuaikan dengan pin GPIO Anda
GPIO.setmode(GPIO.BCM)  # Gunakan penomoran BCM
GPIO.setup(BUZZER_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Hidupkan buzzer
        print("Buzzer ON")  # Debug: Informasikan bahwa buzzer menyala
        time.sleep(1)  # Tunggu 1 detik
        
        GPIO.output(BUZZER_PIN, GPIO.LOW)   # Matikan buzzer
        print("Buzzer OFF")  # Debug: Informasikan bahwa buzzer mati
        time.sleep(1)  # Tunggu 1 detik
except KeyboardInterrupt:
    print("Program dihentikan oleh pengguna.")
finally:
    GPIO.cleanup()  # Pastikan GPIO bersih setelah digunakan
    print("GPIO dibersihkan. Program selesai.")
