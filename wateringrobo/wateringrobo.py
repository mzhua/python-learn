import time

import RPi.GPIO as GPIO

from motor import Motor
from wateringInterface import WateringInterface

STATUS_DEFAULT = 0
STATUS_WATERING = 1


class WateringRobo:
    def __init__(self, pin=27):
        self.waterPinIn = pin

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.waterPinIn, GPIO.IN)

        self.callback = None
        # self.motor = Motor([2, 3, 4, 14])

        self._status = STATUS_DEFAULT

    def _change_status(self, status=STATUS_DEFAULT):
        self._status = status

    def _get_status(self):
        return self._status

    def _watering(self, channel):
        if GPIO.input(channel) == 1:
            print 'start watering'
            if self._get_status() == STATUS_WATERING:
                return
            else:
                self._change_status(STATUS_WATERING)
                self.callback.start_watering()
                # self.motor.turn_with_angel(30)
        else:
            print 'stop watering'
            if self._get_status() == STATUS_DEFAULT:
                return
            else:
                self._change_status(STATUS_DEFAULT)
                self.callback.stop_watering()
                # self.motor.turn_with_angel(-30)

    def start(self, callback):
        if callback is not None:
            if not isinstance(callback, WateringInterface):
                print 'the callback must extend WateringInterface'
                return
            else:
                self.callback = callback
        else:
            self.callback = None

        GPIO.add_event_detect(self.waterPinIn, GPIO.BOTH, self._watering)

        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            print 'bye bye'
        GPIO.remove_event_detect(self.waterPinIn)
