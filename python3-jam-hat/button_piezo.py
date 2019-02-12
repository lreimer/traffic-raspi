import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)

up = 18
down = 19

GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

pwm = GPIO.PWM(20,10)

def buzz(freq,length):
        if not freq:
                pwm.ChangeDutyCycle(0)
        else:
                pwm.ChangeFrequency(freq)
                pwm.ChangeDutyCycle(50)
        sleep(length)
        pwm.ChangeDutyCycle(0)

pwm.start(0)

try:
    while True:
        if GPIO.input(up) or GPIO.input(down):
            if GPIO.input(up):
                while GPIO.input(up):
                    buzz(1046.50,0.1)
            if GPIO.input(down):
                while GPIO.input(down):
                    buzz(261.626,0.1)
        sleep(0.1)
except:
    GPIO.cleanup()
