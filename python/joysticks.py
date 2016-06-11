import time, signal, sys
from Adafruit_ADS1x15 import ADS1x15
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN)
GPIO.setup(31, GPIO.IN)
GPIO.setup(33, GPIO.IN)
GPIO.setup(35, GPIO.IN)

ADS1015 = 0x00   # 12-bit ADC
ADS1115 = 0x01   # 16-bit ADC
gain = 1856.7544
sps = 250

adc = ADS1x15(ic=ADS1115)

while True:
	adc0=adc.readADCSingleEnded(0, gain, sps)/1000
	adc1=adc.readADCSingleEnded(1, gain, sps)/1000
	adc2=adc.readADCSingleEnded(2, gain, sps)/1000
	adc3=adc.readADCSingleEnded(3, gain, sps)/1000
	print str(adc0) + " " + str(adc1) + " " + str(adc2) + " " + str(adc3) + " " + \
		str(GPIO.input(29)) + " " + str(GPIO.input(31)) + " " + \
		str(GPIO.input(33)) + " " + str(GPIO.input(35))
	time.sleep(0.25)
