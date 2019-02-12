import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

SELECT = 18
PLAY = 19
LEDS = (5,12,16,6,13,17)

GPIO.setup(SELECT, GPIO.IN)
GPIO.setup(PLAY, GPIO.IN)
GPIO.setup(LEDS, GPIO.OUT, initial=0)
GPIO.setup(20, GPIO.OUT)

pwm = GPIO.PWM(20,1)
pwm.ChangeDutyCycle(0)

NOTES = [440.000, 391.995, 349.228, 329.628, 293.665, 261.626]

def buzz(freq,length):
        if not freq:
                pwm.ChangeDutyCycle(0)
        else:
                pwm.ChangeFrequency(freq)
                pwm.ChangeDutyCycle(50)
        sleep(length)
        pwm.ChangeDutyCycle(0)

pwm.start(0)

note = 0
GPIO.output(LEDS[note], 1)

try:
    while True:
        if GPIO.input(SELECT):
            if note < 5:
                note += 1
            else:
                note = 0
            GPIO.output(LEDS, 0)
            GPIO.output(LEDS[note], 1)
            while GPIO.input(SELECT):
                sleep(0.1)
        if GPIO.input(PLAY):
            while GPIO.input(PLAY):
                buzz(NOTES[note],0.2)
            sleep(0.1)
except:
    GPIO.cleanup()
