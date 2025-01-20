import RPi.GPIO as GPIO
import time

# Pin GPIO untuk LED
RED_PIN = 10
YELLOW_PIN = 9
GREEN_PIN = 11

def setup_gpio(pins):
    """Inisialisasi GPIO untuk beberapa pin."""
    GPIO.setmode(GPIO.BCM)  # Gunakan penomoran GPIO
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)  # Atur setiap pin sebagai output

def turn_led_on(pin):
    """Menyalakan LED pada pin tertentu."""
    GPIO.output(pin, GPIO.HIGH)  # Nyalakan LED
    print(f"LED pada pin {pin} menyala!")

def turn_led_off(pin):
    """Mematikan LED pada pin tertentu."""
    GPIO.output(pin, GPIO.LOW)  # Matikan LED
    print(f"LED pada pin {pin} mati!")

def clean_gpio():
    """Membersihkan GPIO setelah digunakan."""
    GPIO.cleanup()  # Reset status GPIO
    print("GPIO dibersihkan.")

def blink_leds(pins, blink_interval=1):
    """Mengontrol LED secara bergantian dengan interval tertentu."""
    try:
        while True:
            for pin in pins:
                turn_led_on(pin)
                time.sleep(blink_interval)  # Tunggu interval detik
                turn_led_off(pin)
    except KeyboardInterrupt:
        print("Program dihentikan.")
    finally:
        clean_gpio()

# Main program
if __name__ == "__main__":
    led_pins = [RED_PIN, YELLOW_PIN, GREEN_PIN]
    setup_gpio(led_pins)  # Inisialisasi GPIO untuk semua LED
    blink_interval = 1  # Interval kedipan (detik)
    blink_leds(led_pins, blink_interval)  # Jalankan kontrol LED
