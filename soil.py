import RPi.GPIO as GPIO

import time

#GPIO SETUP

channel = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(channel, GPIO.IN)



while True:



        if GPIO.input(channel):

                print ("water is needed!")

        else:

                print ("Water is not needed")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  

GPIO.add_event_callback(channel, callback)  
