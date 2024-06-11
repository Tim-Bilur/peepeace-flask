import RPi.GPIO as GPIO
import time

# from firebase import get_relayph_value
from firebase import get

# Define the GPIO pin for the LED
LED_PIN = 18


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
            relayph_value = get_relayph_value()

            # Control the LED based on the relayPH value
            control_led(relayph_value)

            # Wait for a while before checking again
            time.sleep(1)

    finally:
        # Clean up GPIO settings
        GPIO.cleanup()


# Run the main function
if __name__ == "__main__":
    main()
