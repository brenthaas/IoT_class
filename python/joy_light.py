import time, signal, sys
from Adafruit_ADS1x15 import ADS1x15
import RPi.GPIO as GPIO

pin_joy_x = 29
pin_joy_y = 35
pin_joy_button = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_joy_x, GPIO.IN)
GPIO.setup(pin_joy_y, GPIO.IN)
GPIO.setup(pin_joy_button, GPIO.IN)

ADS1115 = 0x01   # 16-bit ADC
gain = 1856.7544
sps = 250

adc = ADS1x15(ic=ADS1115)

while True:
	adc2=adc.readADCSingleEnded(2, gain, sps)/1000
	adc3=adc.readADCSingleEnded(3, gain, sps)/1000
	print str(adc2) + " " + str(adc3) + " " + str(GPIO.input(pin_joy_button))
	time.sleep(0.25)
