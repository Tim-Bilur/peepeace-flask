import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize ADS1115 ADC
try:
    ads = ADS.ADS1115(i2c)
    print("ADS1115 successfully initialized")
except Exception as e:
    print(f"Error initializing ADS1115: {e}")
    exit()


# Function to read pH value within a specified duration
def read_ph(timeout=10):
    start_time = time.time()
    last_ph_value = None
    try:
        while time.time() - start_time < timeout:
            chan = AnalogIn(ads, ADS.P0)  # Example: Read from channel 0 (A0)

            # Calibration voltages (adjust these based on your calibration)
            voltage_4 = 3.10
            # Example: Replace with actual voltage for pH 4 calibration
            voltage_7 = (
                2.62  # Example: Replace with actual voltage for pH 7 calibration
            )

            # Calculate pH step
            ph_step = (voltage_4 - voltage_7) / (7 - 4)

            # Read voltage from sensor
            voltage = chan.voltage

            # Calculate pH value
            ph_value = (voltage_7 - voltage) / ph_step

            # Print the pH value during testing
            print(f"Calculated pH: {ph_value:.2f}")

            # Update last_ph_value with the current reading
            last_ph_value = ph_value

            time.sleep(0.5)  # Adjust the sleep duration as needed

    except OSError as e:
        print(f"Error reading pH: {e}")
        return None

    # Return the last pH value read
    return last_ph_value


# If you want to test this script independently, uncomment the next lines:
# if __name__ == "__main__":
#     print("Starting pH sensor readings...")
#     ph_value = read_ph(timeout=10)  # Adjust timeout as needed (default is 10 seconds)
#     if ph_value is not None:
#         print(f"Last pH Value: {ph_value:.2f}")
#     else:
#         print("Failed to read pH value within the specified timeout.")
