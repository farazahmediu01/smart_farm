import Adafruit_DHT
from  time import sleep
from RPi_GPIO_i2c_LCD import lcd

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # Replace with the GPIO pin you've connected the DATA wire to

humidity =0

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(f"Temperature: {temperature:.2f}°C")
        print(f"Humidity: {humidity:.2f}%")
    else:
        print("Failed to retrieve data from the sensor")

   
def MyFunction(self):
    ## Show current time on line 2
    self.lcd.display_string("helllllo",2)
    MyFunction(self)
## Initalize display with callback
lcdDisplay = lcd.HD44780(0x27,MyFunction)

## Set string value to buffer
lcdDisplay.set(str(humidity),1)
sleep(6)
