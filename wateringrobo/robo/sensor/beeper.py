# coding=utf-8
"""
蜂鸣器
"""
import time
import RPi.GPIO as GPIO

from sensorBase import SensorBase
from ..wateringRobo import WateringRobo

from ..util.equip_to import equip_to

_pinNum = None


@equip_to(WateringRobo)
class Beeper(SensorBase):
    def _setup(self):
        GPIO.setmode(GPIO.BCM)

    def beep(self, pin=2, seconds=0.2):
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.output(pin, 0)
        time.sleep(seconds)
        self.mute(pin)

    def mute(self, pin=2):
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.output(pin, 1)
