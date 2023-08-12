import smbus
import time

# Define the I2C bus number (0 or 1)
i2c_bus = 1

# Define the I2C device address (use 'i2cdetect' command to find it)
device_address = 0x48

# Create an instance of the I2C bus
bus = smbus.SMBus(i2c_bus)

try:
    while True:
        # Read the temperature from the I2C device
        temperature = bus.read_word_data(device_address, 0x00)
        temperature = ((temperature << 8) & 0xFF00) + (temperature >> 8)

        # Convert the raw value to Celsius (for TMP102 sensor)
        celsius = (temperature / 256.0) * 0.0625

        print(f"Temperature: {celsius:.2f} °C")
        time.sleep(2)  # Pause for 2 seconds before reading again

except KeyboardInterrupt:
    print("Exiting...")
