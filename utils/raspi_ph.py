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

# Function to calculate pH based on ADC voltage
def read_ph():
    try:
        chan = AnalogIn(ads, ADS.P0)  # Example: Read from channel 0 (A0)

        # Calibration voltages (adjust these based on your calibration)
        voltage_4 = 3.01  # Example: Replace with actual voltage for pH 4 calibration
        voltage_7 = 2.60  # Example: Replace with actual voltage for pH 7 calibration

        # Calculate pH step
        ph_step = (voltage_4 - voltage_7) / (4 - 7)

        # Read voltage from sensor
        voltage = chan.voltage

        # Calculate pH value
        ph_value = 14 + ((voltage_7 - voltage) / ph_step)

        return ph_value

    except OSError as e:
        print(f"Error reading pH: {e}")
        return None

# Example continuous reading from ADS1115
try:
    print("Starting continuous pH readings...")
    while True:
        try:
            ph_value = read_ph()
            if ph_value is not None:
                print(f"Calculated pH: {ph_value:.2f}")
        except OSError as e:
            print(f"Error reading pH: {e}")
        time.sleep(1)  # Adjust as needed for your application

except KeyboardInterrupt:
    print("Program stopped by user.")
