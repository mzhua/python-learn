from sensorBase import SensorBase
import RPi.GPIO as GPIO
from ..util.equip_to import equip_to
from ..wateringRobo import WateringRobo


@equip_to(WateringRobo)
class Pump(SensorBase):
    def start_pump(self, pin=2):
        self._init_gpio(pin, 1)

    def stop_pump(self, pin=2):
        self._init_gpio(pin, 0)

    def _init_gpio(self, pin, level):
        GPIO.setup(pin, GPIO.OUT)
        if GPIO.input(pin) == None:
            print 'please please plug in the water pump in pin ' + str(pin)
        GPIO.output(pin, level)
