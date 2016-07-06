import time

import RPi.GPIO as GPIO

from wateringRoboInterface import WateringRoboInterface

STATUS_DEFAULT = 0
STATUS_WATERING = 1


class WateringRobo:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.callback = None

        self._status = STATUS_DEFAULT

        self.watering_funcs = []
        self.stop_watering_funcs = []

    def _setup_gpio(self, watering_pin):
        self.waterPinIn = watering_pin
        GPIO.setup(self.waterPinIn, GPIO.IN)

    def _change_status(self, status=STATUS_DEFAULT):
        self._status = status

    def _get_status(self):
        return self._status

    def _watering(self, channel):
        if GPIO.input(channel) == 1:
            if self._get_status() == STATUS_WATERING:
                return
            else:
                self._change_status(STATUS_WATERING)
                for func in self.watering_funcs:
                    func()
                # self.callback.start_watering()
        else:
            if self._get_status() == STATUS_DEFAULT:
                return
            else:
                self._change_status(STATUS_DEFAULT)
                for func in self.stop_watering_funcs:
                    func()
                # self.callback.stop_watering()

    def start(self, pin=27, callback=None):
        if callback is not None:
            if not isinstance(callback, WateringRoboInterface):
                print 'the callback must extend WateringInterface'
                return
            else:
                self.callback = callback
        else:
            self.callback = None

        self._setup_gpio(pin)

        GPIO.add_event_detect(self.waterPinIn, GPIO.BOTH, self._watering)

        print 'watering robo started'
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            print 'bye bye'
        self.stop()

    def stop(self):
        self.callback.exit()
        GPIO.remove_event_detect(self.waterPinIn)
        GPIO.cleanup()

    def execute(self, func):
        func(self)

    def do_what_when_need_to_watering(self, watering_funcs=None):
        if watering_funcs is None:
            watering_funcs = []
        self.watering_funcs = watering_funcs

    def do_what_when_need_to_stop_watering(self, stop_watering_funcs=None):
        if stop_watering_funcs is None:
            stop_watering_funcs = []
        self.stop_watering_funcs = stop_watering_funcs

robo = WateringRobo()
