#!/usr/bin/python

from __future__ import print_function
import RPi.GPIO as GPIO
import subprocess, time, Image, socket
from Adafruit_Thermal import *

buttonPin    = 18
holdTime     = 2     # Duration for button hold (shutdown)
tapTime      = 0.01  # Debounce time for button taps
nextInterval = 0.0   # Time of next recurring operation
dailyFlag    = False # Set after daily trigger occurs
lastId       = '1'   # State information passed to/from interval script
printer      = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)


# Initialization

# Use Broadcom pin numbers (not Raspberry Pi pin numbers) for GPIO
GPIO.setmode(GPIO.BCM)

# Enable LED and button (w/pull-up on latter)
GPIO.setup(buttonPin, GPIO.IN)

prevButtonState = GPIO.input(buttonPin)
# Main loop
printer.begin(255)
while(True):
  buttonState = GPIO.input(buttonPin)
  if buttonState != True:
    printer.printImage(Image.open('export.png'), True)
    # printer.printImage(Image.open('emilie-1.png'), True)
    # printer.printImage(Image.open('emilie-0.png'), True)
    printer.feed(3)
    time.sleep(5)
