import RPi.GPIO as GPIO
# import pygame.mixer
# from pygame.mixer import Sound
import time

# pygame.mixer.init()
# drum = Sound("/opt/sonic-pi/etc/samples/bd_boom.flac")

channelIn = 18
channelOut = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(channelIn,GPIO.IN)
GPIO.setup(channelOut,GPIO.OUT)

def beep(argument):
    if GPIO.input(argument) == 0:
        GPIO.output(channelOut,0)
    else:
        GPIO.output(channelOut,1)
    print GPIO.input(channelOut)

GPIO.add_event_detect(channelIn,GPIO.FALLING,callback = beep)

GPIO.output(channelOut,0)
loop = True
try:
    while loop:
		time.sleep(5)
except KeyboardInterrupt:
        loop = False
        GPIO.remove_event_detect(channelIn)
        GPIO.cleanup()
# GPIO.cleanup()

