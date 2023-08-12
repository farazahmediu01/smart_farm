import spidev
import time

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def read_channel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# Define sensor channel
moisture_channel = 0

# Define delay between readings
delay = 2

try:
    while True:
        # Read the moisture sensor data
        moisture_level = read_channel(moisture_channel)

        # Print out result
        print("Moisture Level:", moisture_level)

        # Wait before repeating the loop
        time.sleep(delay)

except KeyboardInterrupt:
    spi.close()

2 