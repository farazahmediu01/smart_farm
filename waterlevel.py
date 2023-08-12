import RPi.GPIO as GPIO
import time

# Set GPIO mode and define the pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
water_level_pin = 27  # GPIO17
buzzer_pin =13   # GPIO18
# Set up the GPIO pins
GPIO.setup(water_level_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)

try:
    while True:
        water_level = GPIO.input(water_level_pin)  # Read the water level sensor state

        if water_level == GPIO.HIGH:
            print("Water level is HIGH - Water Detected")
            GPIO.output(buzzer_pin, GPIO.HIGH)  # Turn on the buzzer
        else:
            print("Water level is LOW - No Water Detected")
            GPIO.output(buzzer_pin, GPIO.LOW)  # Turn off the buzzer

        time.sleep(2)  # Pause for 2 seconds before reading again

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()  # Clean up GPIO settings on exit