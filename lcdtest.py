import Adafruit_DHT
from  time import sleep
import board
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd


# Initialize the DHT11 sensor.
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

# Initialize the I2C LCD display.
lcd_columns = 16  # Number of columns on the LCD
lcd_rows = 2     # Number of rows on the LCD
i2c = board.I2C()  # Initialize I2C bus
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows)

try:
    while True:
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            if humidity is not None and temperature is not None:
                print(f"Temperature: {temperature:.2f}°C")
                lcd.message(f"Temperature: {temperature:.2f}°C")
                print(f"Humidity: {humidity:.2f}%")
                lcd.message(f"Humidity: {humidity:.2f}%")
            else:
                print("Failed to retrieve data from the sensor")
                lcd.message("Sensor Error!")

        # Display temperature and humidity on the LCD.
            lcd.clear()

        # Wait for a short interval before updating the display again.
            time.sleep(2)

except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
