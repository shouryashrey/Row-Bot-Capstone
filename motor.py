import RPi.GPIO as gpio
import time

# gpio.setmode(gpio.BOARD)

in1 = 16
in2 = 18

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(in1, gpio.OUT)
    gpio.setup(in2, gpio.OUT)

def clockwise(sec):
    init()
    gpio.output(in1, True)
    gpio.output(in2, False)
    time.sleep(sec)
    gpio.cleanup()

def anticlockwise(sec):
    init()
    gpio.output(in1, False)
    gpio.output(in2, True)
    time.sleep(sec)
    gpio.cleanup()

# clockwise(3)
# anticlockwise(3)