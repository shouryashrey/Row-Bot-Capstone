import RPi.GPIO as gpio
import time


redled = 3
greenled = 5

# gpio.setup(redled, gpio.OUT)
# gpio.setup(greenled, gpio.OUT)
# gpio.output(redled, 0)
# gpio.output(greenled, 0)

def redHIGH():
    gpio.setmode(gpio.BOARD)
    gpio.setup(redled, gpio.OUT)
    gpio.output(redled, 0)

    gpio.output(redled, 1)
    time.sleep(3)
    gpio.output(redled, 0)

def greenHIGH():
    gpio.setmode(gpio.BOARD)
    gpio.setup(greenled, gpio.OUT)
    gpio.output(greenled, 0)

    gpio.output(greenled, 1)
    time.sleep(3)
    gpio.output(greenled, 0)

def redLOW():
    gpio.setmode(gpio.BOARD)
    gpio.setup(redled, gpio.OUT)
    gpio.output(redled, 0)

    # gpio.output(redled, 1)
    # time.sleep(3)
    # gpio.output(redled, 0)

def greenLOW():
    gpio.setmode(gpio.BOARD)
    gpio.setup(greenled, gpio.OUT)
    gpio.output(greenled, 0)

    # gpio.output(greenled, 1)
    # time.sleep(3)
    # gpio.output(greenled, 0)


# red()
# green()
