import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
moisture_pin = 17  # GPIO17 (or any other available GPIO pin)

GPIO.setup(moisture_pin, GPIO.IN)

try:
    while True:
        moisture_level = GPIO.input(moisture_pin)
        if moisture_level == GPIO.LOW:
            print("Soil is moist")
        else:
            print("Soil is dry")
        time.sleep(2)  # Pause for 2 seconds before reading again

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
