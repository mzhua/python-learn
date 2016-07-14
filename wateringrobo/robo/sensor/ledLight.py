"""
led
"""
import RPi.GPIO as GPIO

from sensorBase import SensorBase
from ..util.equip_to import equip_to
from ..wateringRobo import WateringRobo


@equip_to(WateringRobo)
class LedLight(SensorBase):

    def light_on(self, pin=17):
        print 'light on'
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 1)

    def light_off(self, pin=17):
        print 'light off'
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
