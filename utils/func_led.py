import RPi.GPIO as GPIO
import time

# Pin GPIO yang digunakan
PIN = 6

def setup_gpio(pin):
    """Inisialisasi GPIO untuk pin tertentu."""
    GPIO.setmode(GPIO.BCM)  # Gunakan penomoran GPIO
    GPIO.setup(pin, GPIO.OUT)  # Atur pin sebagai output

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

def led_blink(pin, blink_interval=1):
    """Menyala dan mematikan LED secara bergantian dengan interval tertentu."""
    try:
        while True:
            turn_led_on(pin)
            time.sleep(blink_interval)  # Tunggu selama interval detik
            
            turn_led_off(pin)
            time.sleep(blink_interval)  # Tunggu selama interval detik
    except KeyboardInterrupt:
        print("Program dihentikan.")
    finally:
        clean_gpio()

# Main program
if __name__ == "__main__":
    setup_gpio(PIN)  # Inisialisasi GPIO untuk pin
    led_blink(PIN)  # Mulai mengedipkan LED
