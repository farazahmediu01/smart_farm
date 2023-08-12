from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from threading import Thread
from gpiozero import DistanceSensor
from rpi_lcd import LCD

reading = True
message = ""

lcd = LCD()
sensor = DistanceSensor(echo=20, trigger=21)

def safe_exit(signum, frame):
    exit(1)

def display_distance():
    while reading:
        lcd.text(message, 1)
        sleep(0.25)

def read_distance():
    global message

    while reading:
        message = "Distance"
        print(message)

        sleep(0.1)

try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)

    reader = Thread(target=read_distance, daemon=True)
    display = Thread(target=display_distance, daemon=True)

    reader.start()
    display.start()

    pause()

except KeyboardInterrupt:
    pass

finally:
    reading = False
    reader.join()
    display.join()
    lcd.clear()
    sensor.close()