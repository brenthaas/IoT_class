import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

speed=0.5

while True:
    GPIO.output(11, True)
    time.sleep(speed)
    GPIO.output(11, False)
    time.sleep(speed)
    GPIO.output(13, True)
    time.sleep(speed)
    GPIO.output(13, False)
    time.sleep(speed)
    GPIO.output(15, True)
    time.sleep(speed)
    GPIO.output(15, False)
    time.sleep(speed)
