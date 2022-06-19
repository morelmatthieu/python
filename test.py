import RPi.GPIO as GPIO
import random,time

def allumage(LED):
    print(LED)
    
    GPIO.output(LED,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED,GPIO.LOW)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
vert = 11
orange = 13
rouge = 15
a = 0

try:
    while True:
        a = a + 1
        if a == 4:
            a = 1
        if a == 1:
            LED = vert
        elif a == 2:
            LED = orange
        elif a == 3:
            LED = rouge
        allumage (LED)
except KeyboardInterrupt:
    GPIO.output(LED,GPIO.LOW)
    GPIO.cleanup()