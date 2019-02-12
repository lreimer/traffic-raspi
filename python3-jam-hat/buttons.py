from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

up = 18
down = 19

GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

try:
    counter = 0
    while True:
        if GPIO.input(up) or GPIO.input(down):
            if GPIO.input(up):
                counter += 1
                while GPIO.input(up):
                    sleep(0.1)
            if GPIO.input(down):
                counter -= 1
                while GPIO.input(down):
                    sleep(0.1)
            print "Counter: %d" % counter
        sleep(0.1)
except:
    GPIO.cleanup()
