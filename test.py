import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # Replace with the GPIO pin you've connected the DATA wire to

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

if humidity is not None and temperature is not None:
    print(f"Temperature: {temperature:.2f}°C")
    print(f"Humidity: {humidity:.2f}%")
else:
    print("Failed to retrieve data from the sensor")
