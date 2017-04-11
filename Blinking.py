#!/usr/bin/python
import RPi.GPIO as GPIO     ##Import GPIO Library
import time                 ##Import time Library untuk sleep

GPIO.setmode(GPIO.BCM)      ##Guna GPIO pin numbering
GPIO.setwarnings(False)     ##Disable Warning
GPIO.setup(2,GPIO.OUT)      ##Set output
for _ in range(10):          
  GPIO.output(2, True)      ##LED ON
  time.sleep(0.5)           ##Pause 5 sec
  GPIO.output(2, False)     ##LED OFF
  time.sleep(0.5)           ##Pause 5 sec

GPIO.cleanup()              ##Reset GPIO


