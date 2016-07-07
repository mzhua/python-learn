"""
led
"""
import RPi.GPIO as GPIO
from sensorBase import SensorBase
from ..wateringRobo import WateringRobo

from ..util.equip_to import equip_to


@equip_to(WateringRobo)
class LedLight(SensorBase):
    def _setup(self):
        GPIO.setmode(GPIO.BCM)

    def light(self, on=True, pin=17):
        GPIO.setup(pin, GPIO.OUT)

        if on:
            GPIO.output(pin, 1)
        else:
            GPIO.output(pin, 0)
