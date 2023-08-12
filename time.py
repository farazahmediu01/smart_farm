from RPi_GPIO_i2c_LCD import lcd
from time import sleep, strftime
import Adafruit_DHT

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