#!/usr/bin/python
from __future__ import print_function
import RPi.GPIO as GPIO
import subprocess, time, Image, socket
from Adafruit_Thermal import *

printer      = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
printer.begin(60)
printer.printImage(Image.open('gfx/hello.png'), True)
printer.print('Hello World blabla blabla blabla')
printer.feed(3)
