import time

import RPi.GPIO as GPIO

STATUS_DEFAULT = 0
STATUS_WATERING = 1


class WateringRobo(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self._status = STATUS_DEFAULT

        self.watering_funcs = []
        self.stop_watering_funcs = []

    def _setup_gpio(self, watering_pin):
        self.waterPinIn = watering_pin
        GPIO.setup(self.waterPinIn, GPIO.IN)
        GPIO.add_event_detect(self.waterPinIn, GPIO.BOTH, self._watering)

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
        else:
            if self._get_status() == STATUS_DEFAULT:
                return
            else:
                self._change_status(STATUS_DEFAULT)
                for func in self.stop_watering_funcs:
                    func()

    def start(self, pin=27):

        self._setup_gpio(pin)

        print 'watering robo started'
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            print 'bye bye'
        self.stop()

    def stop(self):
        GPIO.remove_event_detect(self.waterPinIn)
        GPIO.cleanup()

    def execute(self, func):
        func(self)

    def do_what_when_need_to_watering(self, watering_func=None):
        self.watering_funcs.append(watering_func)

    def do_what_when_stop_watering(self, stop_watering_func=None):
        self.stop_watering_funcs.append(stop_watering_func)
