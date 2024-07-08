import RPi.GPIO as GPIO
import keyboard
import time

# Nomor pin yang digunakan
LED_PIN = 16

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)  # Gunakan penomoran GPIO.BCM
GPIO.setup(LED_PIN, GPIO.OUT)  # Set pin sebagai output

try:
    # Nyalakan LED
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("LED ON")
    
    while True:
        # Cek apakah tombol 'e' ditekan
        if keyboard.is_pressed('e'):
            print("Tombol 'e' ditekan, mematikan LED dan menghentikan program...")
            break
        time.sleep(0.1)  # Tunggu sebentar sebelum cek lagi

except KeyboardInterrupt:
    print("Program dihentikan oleh pengguna")

finally:
    # Matikan LED dan reset konfigurasi GPIO
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
    print("LED OFF, GPIO dibersihkan")
