import RPi.GPIO as GPIO
import time

# Pin GPIO yang digunakan
pin = 6

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Gunakan penomoran GPIO
GPIO.setup(pin, GPIO.OUT)  # Atur pin 6 sebagai output

try:
    while True:
        # Nyalakan LED pada pin 6
        GPIO.output(pin, GPIO.HIGH)
        print("LED pada pin 6 menyala!")
        time.sleep(1)  # Tunggu 1 detik

        # Matikan LED pada pin 6
        GPIO.output(pin, GPIO.LOW)
        print("LED pada pin 6 mati!")
        time.sleep(1)  # Tunggu 1 detik sebelum mengulang

except KeyboardInterrupt:
    print("Program dihentikan.")
finally:
    GPIO.cleanup()  # Reset status GPIO
