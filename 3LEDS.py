# fait clignoter 3 LEDS en boucle sur pins 11, 13, 15 quand un bouton branché sur pin 12 est pressé
# servo sur 18
import RPi.GPIO as GPIO
import time
#  ---fonction allumage-extinction
def allumage(LED):
    print('broche activée : ',LED[0],' --> couleur : ',LED[1])
    GPIO.output(LED[0],GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(LED[0],GPIO.LOW)
#  ---setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT) #LED verte
GPIO.setup(13,GPIO.OUT) #LED orange
GPIO.setup(15,GPIO.OUT) #LED rouge
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP) # bouton poussoir
GPIO.setup(18,GPIO.OUT) #servo

bouton=12
vert = [11,'vert']
orange = [13,'orange']
rouge = [15,'rouge']
pwm_servo = GPIO.PWM(18,50)
pwm_servo.start(5)
print('démarrage programme')
#  ---programe---
a = 0
try:
    while True:
        while GPIO.input(bouton) == 0:
            a = a + 1
            if a == 4:
                a = 1
            if a == 1:
                LED = vert
                pwm_servo.ChangeDutyCycle(5)
            elif a == 2:
                LED = orange
                pwm_servo.ChangeDutyCycle(7.5)
            elif a == 3:
                LED = rouge
                pwm_servo.ChangeDutyCycle(10)
            allumage (LED)
except KeyboardInterrupt:
    GPIO.output(LED[0],GPIO.LOW)
    GPIO.cleanup()
