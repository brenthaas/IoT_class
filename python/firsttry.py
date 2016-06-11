#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
import pyfirmata, time

port = '/dev/tty.usbserial-A50285BI'

board = pyfirmata.Arduino(port)
it = pyfirmata.util.Iterator(board)
it.start

button_pin = board.get_pin('d:10:i')
blink_pin = board.get_pin('d:13:o')

while True:
    button_pressed = button_pin.read()
    if button_pressed > 0:
        blink_pin.write(1)
        time.sleep(1)
        blink_pin.write(0)
        time.sleep(1)
