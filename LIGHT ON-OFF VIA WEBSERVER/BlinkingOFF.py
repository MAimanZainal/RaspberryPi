#!/usr/bin/python
import RPi.GPIO as GPIO     ##Import GPIO Library
import time                 ##Import time Library untuk sleep

GPIO.setmode(GPIO.BCM)      ##Guna GPIO pin numbering
GPIO.setwarnings(False)     ##Block Warning 
GPIO.setup(2,GPIO.OUT)      ##Set output



def trigger():
    GPIO.output(2,False)    ##LED OFF
try:
    trigger()

except KeyboardInterrupt:
    print ("Quit")
    GPIO.cleanup()          ##Reset GPIO

