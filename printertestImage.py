#!/usr/bin/python

from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

printer.setDefault()
printer.setTimes(33000, 2500)

# CODE39 is the most common alphanumeric barcode
printer.printBarcode("ADAFRUT", printer.CODE39)
printer.setBarcodeHeight(100)
# Print UPC line on product barcodes
printer.printBarcode("123456789123", printer.UPC_A)

# Print the 75x75 pixel logo in adalogo.py
import gfx.adalogo as adalogo
printer.printBitmap(adalogo.width, adalogo.height, adalogo.data)

# Print the 135x135 pixel QR code in adaqrcode.py
import gfx.adaqrcode as adaqrcode
printer.printBitmap(adaqrcode.width, adaqrcode.height, adaqrcode.data)
printer.println("Adafruit!")
printer.feed(1)

printer.sleep()      # Tell printer to sleep
printer.wake()       # Call wake() before printing again, even if reset
printer.setDefault() # Restore printer to defaults
