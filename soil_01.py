import spidev
import time

# Define SPI settings
SPI_PORT = 0
SPI_DEVICE = 0
spi = spidev.SpiDev()
spi.open(SPI_PORT, SPI_DEVICE)
spi.max_speed_hz = 1000000  # You might need to adjust this speed based on your sensor's specifications

def read_adc(channel):
    # MCP3008 has 8 channels (0-7)
    if channel < 0 or channel > 7:
        raise ValueError("Invalid ADC channel. Must be between 0 and 7.")
    
    # Build SPI data
    adc_data = spi.xfer2([7, (8 + channel) << 4, 0])
    
    # Extract raw ADC value from returned data
    raw_adc = ((adc_data[1] & 3) << 8) + adc_data[2]
    return raw_adc

def convert_to_percentage(raw_adc_value):
    # Convert raw ADC value to percentage
    percentage = ((1023 - raw_adc_value) / 1023) * 100
    return percentage

try:
    while True:
        # Assuming you're using channel 0 on MCP3008 for the soil moisture sensor
        channel = 0
        raw_adc_value = read_adc(channel)
        moisture_percentage = convert_to_percentage(raw_adc_value)
        
        print(f"Soil Moisture: {moisture_percentage:.2f}%")
        
        time.sleep(2)  # Delay before the next reading

except KeyboardInterrupt:
    pass

finally:
    spi.close()
