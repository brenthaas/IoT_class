#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
import pyfirmata, time

port = '/dev/tty.usbserial-A50285BI'

board = pyfirmata.Arduino(port)
it = pyfirmata.util.Iterator(board)
it.start

red = board.get_pin('d:6:p')
blue = board.get_pin('d:5:p')
green = board.get_pin('d:3:p')
button = board.get_pin('d:10:i')

pulse_length = 1
green.write(1)
blue.write(1)
while True:
    red.write(1)
    time.sleep(pulse_length)
    red.write(0)
    time.sleep(pulse_length)
