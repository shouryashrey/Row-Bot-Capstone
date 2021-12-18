import cv2
from lobe import ImageModel
import RPi.GPIO as gpio
import time
import ultrasonic as ul
import motor
import blinkLED as led
import findmylocation as gps

print("Importing done")

bioGarbage = ["cardboard","paper"]
nonbioGarbage = ["glass","metal","plastic","trash"]

cam = cv2.VideoCapture(0)

# cv2.namedWindow("test")

model = ImageModel.load('model')

print("Model loaded")
led.greenLOW()
led.redLOW()

while True:
    gpio.cleanup()
    # gpio.setmode(gpio.BOARD)
    # gpio.output(3,0)
    # gpio.output(5,0)
    led.greenLOW()
    led.redLOW()
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break
    # cv2.imshow("test",frame)

    k = cv2.waitKey(1)

    if k%256 == 27:
        print("Esc hit, closing...")
        break
    elif ul.distance() <= 8:
        time.sleep(3)
        img_name = "garbage.png"
        cv2.imwrite("image/"+img_name,frame)
        result = model.predict_from_file('image/garbage.png')
        # predict_path = "prediction/"+"predicted_As_"+result.prediction+".png"
        # cv2.imwrite(predict_path,frame)
        print("Garbage Detected Successfully\n")
        print(result.prediction)
        garbageType = result.prediction

        seconds = 3
        time.sleep(seconds)
        # print("forward")
        if(result.prediction in bioGarbage):
            print("\nGarbage Type : Biodegradable")
            led.greenHIGH()
            print("\nGarbage is put in the biodegradable bin")
            motor.clockwise(seconds)
            time.sleep(seconds-2)
        elif(result.prediction in nonbioGarbage):
            print("Garbage Type : Non-biodegradable")
            led.redHIGH()
            print("\nGarbage is put in the non-biodegradable bin")
            motor.anticlockwise(seconds)
            time.sleep(seconds-2)
        else:
            pass
        # print("reverse")
        print("\nCurrent Location")
        gps.location()

        print("\nDONE\n")


cam.release()

cv2.destroyAllWindows()
