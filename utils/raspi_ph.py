from time import sleep
from gpiozero import MCP3008

# Initialize ADC
adc = MCP3008()

try:
    while True:
        # Read analog input from channel 0 (A0)
        value = adc.value
        
        # Convert analog value to pH (adjust as per your calibration)
        pH = value * 3.3 / 1023.0
        
        print("pH:", pH)
        sleep(1)
except KeyboardInterrupt:
    pass
