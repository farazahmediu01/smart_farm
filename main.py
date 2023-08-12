# DHT11 with I2C LCD
from RPi_GPIO_i2c_LCD import lcd
from time import sleep, strftime
import Adafruit_DHT
import time
# Water Level
import RPi.GPIO as GPIO

# Water Level start
# Set GPIO mode and define the pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
water_level_pin = 27  # GPIO17
buzzer_pin =13   # GPIO18
# Set up the GPIO pins
GPIO.setup(water_level_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)
# Water Level end

#Soil Moisture start
moisture_pin = 22  # GPIO17 (or any other available GPIO pin)

GPIO.setup(moisture_pin, GPIO.IN)
#Soil Moisture end

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  
## Callback function that will run on every display loop
humidity =0
def MyFunction(self):
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print(f"Temperature: {temperature:.2f}°C")
            print(f"Humidity: {humidity:.2f}%")
            ## Show current time on line 2
            self.lcd.display_string("Humidity "+str(humidity),1)
            self.lcd.display_string("Temprature "+str(temperature),2)
            sleep(1)

## Initalize display with callback
lcdDisplay = lcd.HD44780(0x27,MyFunction)

## Set string value to buffer
sleep(2)
try:
    while True:
        water_level = GPIO.input(water_level_pin)  # Read the water level sensor state

        if water_level == GPIO.HIGH:
            print("Water level is HIGH - Water Detected")
            GPIO.output(buzzer_pin, GPIO.HIGH)  # Turn on the buzzer
        else:
            print("Water level is LOW - No Water Detected")
            GPIO.output(buzzer_pin, GPIO.LOW)  # Turn off the buzzer

        sleep(2)  # Pause for 2 seconds before reading again
        moisture_level = GPIO.input(moisture_pin)
        if moisture_level == GPIO.LOW:
            print("Soil is moist")
        else:
            print("Soil is dry")
        time.sleep(2)  # Pause for 2 seconds before reading again
        # Moisture sensor
  # Pause for 2 seconds before reading again


except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()  # Clean up GPIO settings on exit