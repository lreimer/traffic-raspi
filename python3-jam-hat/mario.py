import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)

pwm = GPIO.PWM(20,100)

NOTE_A0=27.5000
NOTE_AS0=29.1353
NOTE_B0=30.8677
NOTE_C1=32.7032
NOTE_CS1=34.6479
NOTE_D1=36.7081
NOTE_DS1=38.8909
NOTE_E1=41.2035
NOTE_F1=43.6536
NOTE_FS1=46.2493
NOTE_G1=48.9995
NOTE_GS1=51.9130
NOTE_A1=55.0000
NOTE_AS1=58.2705
NOTE_B1=61.7354
NOTE_C2=65.4064
NOTE_CS2=69.2957
NOTE_D2=73.4162
NOTE_DS2=77.7817
NOTE_E2=82.4069
NOTE_F2=87.3071
NOTE_FS2=92.4986
NOTE_G2=97.9989
NOTE_GS2=103.826
NOTE_A2=110.000
NOTE_AS2=116.541
NOTE_B2=123.471
NOTE_C3=130.813
NOTE_CS3=138.591
NOTE_D3=146.832
NOTE_DS3=155.563
NOTE_E3=164.814
NOTE_F3=174.614
NOTE_FS3=184.997
NOTE_G3=195.998
NOTE_GS3=207.652
NOTE_A3=220.000
NOTE_AS3=233.082
NOTE_B3=246.942
NOTE_C4=261.626
NOTE_CS4=277.183
NOTE_D4=293.665
NOTE_DS4=311.127
NOTE_E4=329.628
NOTE_F4=349.228
NOTE_FS4=369.994
NOTE_G4=391.995
NOTE_GS4=415.305
NOTE_A4=440.000
NOTE_AS4=466.164
NOTE_B4=493.883
NOTE_C5=523.251
NOTE_CS5=554.365
NOTE_D5=587.330
NOTE_DS5=622.254
NOTE_E5=659.255
NOTE_F5=698.456
NOTE_FS5=739.989
NOTE_G5=783.991
NOTE_GS5=830.609
NOTE_A5=880.000
NOTE_AS5=932.328
NOTE_B5=987.767
NOTE_C6=1046.50
NOTE_CS6=1108.73
NOTE_D6=1174.66
NOTE_DS6=1244.51
NOTE_E6=1318.51
NOTE_F6=1396.91
NOTE_FS6=1479.98
NOTE_G6=1567.98
NOTE_GS6=1661.22
NOTE_A6=1760.00
NOTE_AS6=1864.66
NOTE_B6=1975.53
NOTE_C7=2093.00
NOTE_CS7=2217.46
NOTE_D7=2349.32
NOTE_DS7=2489.02
NOTE_E7=2637.02
NOTE_F7=2793.83
NOTE_FS7=2959.96
NOTE_G7=3135.96
NOTE_GS7=3322.44
NOTE_A7=3520.00
NOTE_AS7=3729.31
NOTE_B7=3951.07
NOTE_C8=4186.01
NOTE_CS8=4435
NOTE_D8=4699
NOTE_DS8=4978

melody = [NOTE_E7, NOTE_E7, 0, NOTE_E7,0, NOTE_C7, NOTE_E7, 0,NOTE_G7, 0, 0,  0,NOTE_G6, 0, 0, 0,NOTE_C7, 0, 0, NOTE_G6,0, 0, NOTE_E6, 0,0, NOTE_A6, 0, NOTE_B6,0, NOTE_AS6, NOTE_A6, 0,NOTE_G6, NOTE_E7, NOTE_G7,NOTE_A7, 0, NOTE_F7, NOTE_G7,0, NOTE_E7, 0, NOTE_C7,NOTE_D7, NOTE_B6, 0, 0,NOTE_C7, 0, 0, NOTE_G6,0, 0, NOTE_E6, 0,0, NOTE_A6, 0, NOTE_B6,0, NOTE_AS6, NOTE_A6, 0,NOTE_G6, NOTE_E7, NOTE_G7,NOTE_A7, 0, NOTE_F7, NOTE_G7,0, NOTE_E7, 0, NOTE_C7,NOTE_D7, NOTE_B6, 0, 0]
tempo = [12, 12, 12, 12,12, 12, 12, 12,12, 12, 12, 12,12, 12, 12, 12,12, 12, 12, 12,12, 12, 12, 12,12, 12, 12, 12,12, 12, 12, 12,9, 9, 9,12, 12, 12, 12,12, 12, 12, 12,12, 12, 12, 12,12, 12, 12, 12,12, 12, 12, 12,12, 12, 12, 12,12, 12, 12, 12,9, 9, 9,12, 12, 12, 12,12, 12, 12, 12,12, 12, 12, 12]

underworld_melody = [
  NOTE_C4, NOTE_C5, NOTE_A3, NOTE_A4,
  NOTE_AS3, NOTE_AS4, 0,
  0,
  NOTE_C4, NOTE_C5, NOTE_A3, NOTE_A4,
  NOTE_AS3, NOTE_AS4, 0,
  0,
  NOTE_F3, NOTE_F4, NOTE_D3, NOTE_D4,
  NOTE_DS3, NOTE_DS4, 0,
  0,
  NOTE_F3, NOTE_F4, NOTE_D3, NOTE_D4,
  NOTE_DS3, NOTE_DS4, 0,
  0, NOTE_DS4, NOTE_CS4, NOTE_D4,
  NOTE_CS4, NOTE_DS4,
  NOTE_DS4, NOTE_GS3,
  NOTE_G3, NOTE_CS4,
  NOTE_C4, NOTE_FS4, NOTE_F4, NOTE_E3, NOTE_AS4, NOTE_A4,
  NOTE_GS4, NOTE_DS4, NOTE_B3,
  NOTE_AS3, NOTE_A3, NOTE_GS3,
  0, 0, 0]

underworld_tempo = [
  12, 12, 12, 12,
  12, 12, 6,
  3,
  12, 12, 12, 12,
  12, 12, 6,
  3,
  12, 12, 12, 12,
  12, 12, 6,
  3,
  12, 12, 12, 12,
  12, 12, 6,
  6, 18, 18, 18,
  6, 6,
  6, 6,
  6, 6,
  18, 18, 18, 18, 18, 18,
  10, 10, 10,
  10, 10, 10,
  3, 3, 3]
  
def buzz(freq,length):
        if not freq:
                pwm.ChangeDutyCycle(0)
        else:
                pwm.ChangeFrequency(freq)
                pwm.ChangeDutyCycle(50)
        sleep(length)
        pwm.ChangeDutyCycle(0)

def sing(s):
        if s == 1:
                size = len(melody)
                note = 0
                while(note<size):
                        duration = 1 / float(tempo[note])
                        buzz(melody[note],duration)
                        sleep(duration*1.3)
                        note+=1
        else:
                size = len(underworld_melody)
                note = 0
                while(note<size):
                        duration = 1 / float(underworld_tempo[note])
                        buzz(underworld_melody[note],duration)
                        sleep(duration*1.3)
                        note+=1
						
try:
	pwm.start(0)
	sing(1)
	sing(2)
except:
	pwm.stop()
	GPIO.cleanup()
