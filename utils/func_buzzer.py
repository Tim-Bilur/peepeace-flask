import RPi.GPIO as GPIO
import time

# Konfigurasi pin
BUZZER_PIN = 16  # Sesuaikan dengan pin GPIO Anda


def setup_gpio():
    """Inisialisasi GPIO untuk buzzer."""
    GPIO.setmode(GPIO.BCM)  # Gunakan penomoran BCM
    GPIO.setup(BUZZER_PIN, GPIO.OUT)


def turn_buzzer_on():
    """Menyalakan buzzer."""
    GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Hidupkan buzzer
    print("Buzzer ON")  # Debug: Informasikan bahwa buzzer menyala


def turn_buzzer_off():
    """Mematikan buzzer."""
    GPIO.output(BUZZER_PIN, GPIO.LOW)  # Matikan buzzer
    print("Buzzer OFF")  # Debug: Informasikan bahwa buzzer mati


def clean_gpio():
    """Membersihkan GPIO setelah digunakan."""
    GPIO.cleanup()  # Pastikan GPIO bersih setelah digunakan
    print("GPIO dibersihkan. Program selesai.")


def beep_once():
    """Menyalakan buzzer sekali sebagai alert."""
    try:
        setup_gpio()  # Inisialisasi GPIO
        turn_buzzer_on()
        time.sleep(1)  # Tahan selama 1 detik atau sesuai kebutuhan Anda
        turn_buzzer_off()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        clean_gpio()  # Bersihkan GPIO


# # Main program
if __name__ == "__main__":
    beep_once()
