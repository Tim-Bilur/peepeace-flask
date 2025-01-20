import RPi.GPIO as GPIO

# Define LED pins
LED_PINS = {
    "red": 10,
    "yellow": 9,
    "green": 11,
}

# Internal flag to check GPIO setup status
GPIO_INITIALIZED = False

def setup_gpio():
    """Initialize GPIO pins for LEDs."""
    global GPIO_INITIALIZED
    if not GPIO_INITIALIZED:
        GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
        for pin in LED_PINS.values():
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        GPIO_INITIALIZED = True
        print("GPIO initialized.")

def clean_gpio():
    """Clean up GPIO settings."""
    global GPIO_INITIALIZED
    if GPIO_INITIALIZED:
        GPIO.cleanup()
        GPIO_INITIALIZED = False
        print("GPIO cleaned up.")

def led_green_on():
    """Turn on the green LED."""
    setup_gpio()  # Ensure GPIO is set up
    GPIO.output(LED_PINS["green"], GPIO.HIGH)
    print("Green LED ON.")

def led_green_off():
    """Turn off the green LED."""
    setup_gpio()  # Ensure GPIO is set up
    GPIO.output(LED_PINS["green"], GPIO.LOW)
    print("Green LED OFF.")

def led_red_on():
    """Turn on the red LED."""
    setup_gpio()  # Ensure GPIO is set up
    GPIO.output(LED_PINS["red"], GPIO.HIGH)
    print("Red LED ON.")

def led_red_off():
    """Turn off the red LED."""
    setup_gpio()  # Ensure GPIO is set up
    GPIO.output(LED_PINS["red"], GPIO.LOW)
    print("Red LED OFF.")

def led_yellow_on():
    """Turn on the yellow LED."""
    setup_gpio()  # Ensure GPIO is set up
    GPIO.output(LED_PINS["yellow"], GPIO.HIGH)
    print("Yellow LED ON.")

def led_yellow_off():
    """Turn off the yellow LED."""
    setup_gpio()  # Ensure GPIO is set up
    GPIO.output(LED_PINS["yellow"], GPIO.LOW)
    print("Yellow LED OFF.")
