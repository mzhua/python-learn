"""
led
"""
import RPi.GPIO as GPIO

from rpiBase import RPiBase


class LedLight(RPiBase):
    def __init__(self):
        RPiBase.__init__(self)
        GPIO.setup(17, GPIO.OUT)

    def light(self, on=True):
        if on:
            GPIO.output(17, 1)
        else:
            GPIO.output(17, 0)
        print 'light ' + ('on' if on else 'off')
