import RPi.GPIO as GPIO


class SensorBase:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        print 'GPIO initial'