import RPi.GPIO as GPIO
import time
from firebase2 import get_relayph_from_firebase, update_relayph_in_firebase

# Define the GPIO pin for the LED
LED_PIN = 18

# CHANGE THE LINK
FIREBASE_URL = "https://peepeace-app-default-rtdb.asia-southeast1.firebasedatabase.app/urine_reports.json"  # Replace with your Firebase URL


def setup_gpio():
    """
    Set up the GPIO pin for the LED.
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)


def control_led(state):
    """
    Control the LED based on the state.

    Args:
    state (bool): If True, turn the LED on. If False, turn the LED off.
    """
    if state:
        GPIO.output(LED_PIN, GPIO.HIGH)  # LED ON
    else:
        GPIO.output(LED_PIN, GPIO.LOW)  # LED OFF


def main():
    # Set up GPIO
    setup_gpio()

    try:
        while True:
            # Get the relayPH value from Firebase
            relayph_value = get_relayph_from_firebase(FIREBASE_URL)

            # Control the LED based on the relayPH value
            if relayph_value:
                control_led(True)  # Turn LED on if relayPH is True
            else:
                control_led(False)  # Turn LED off if relayPH is False

            # Wait for a while before checking again
            time.sleep(1)

    finally:
        # Clean up GPIO settings
        GPIO.cleanup()


# Run the main function
if __name__ == "__main__":
    main()

