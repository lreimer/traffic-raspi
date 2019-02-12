from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

LEDS = (5,12,16,6,13,17)

GPIO.setup(LEDS, GPIO.OUT, initial=0)

try:
        prev = 0
        led_length = len(LEDS)
        while True:
                for i in range(led_length):
                        GPIO.output(LEDS[prev],0)
                        GPIO.output(LEDS[i],1)
                        prev = i
                        sleep(.2)
except:
        GPIO.cleanup()
