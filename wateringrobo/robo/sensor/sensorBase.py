import RPi.GPIO as GPIO

class SensorBase(object):
    def _setup(self):
        GPIO.setmode(GPIO.BCM)
