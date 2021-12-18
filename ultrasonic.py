import RPi.GPIO as GPIO
import time


print("Starting Measurement....")

def distance():
    GPIO.setmode(GPIO.BOARD)

    trig = 40
    echo = 38

    GPIO.setup(trig, GPIO.OUT)
    GPIO.output(trig, 0)

    GPIO.setup(echo, GPIO.IN)
    time.sleep(0.1)

    # print("setup complete")

    GPIO.output(trig, 1)
    time.sleep(0.00001)
    GPIO.output(trig, 0)

    # print("trigerred")

    while(GPIO.input(echo) == 0):
        pass

    start = time.time()
    while(GPIO.input(echo) == 1):
        pass
    stop = time.time()

    # print("input received")

    print((stop - start)*17000," cm")
    time.sleep(0.5)
    GPIO.cleanup()
    return ((stop - start)*17000)

# distance()