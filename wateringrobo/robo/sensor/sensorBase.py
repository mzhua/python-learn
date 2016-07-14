import RPi.GPIO as GPIO
import atexit

atexit.register(GPIO.cleanup)


class SensorBase(object):
    def _setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
