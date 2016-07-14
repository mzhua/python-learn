import time
import functools
from command import Command
import RPi.GPIO as GPIO
import threading

import atexit

atexit.register(GPIO.cleanup)

STATUS_DEFAULT = 0
STATUS_WATERING = 1

mutex = threading.Lock()


class WateringRobo(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self._status = STATUS_DEFAULT

        self.watering_funcs = []
        self.stop_watering_funcs = []

    def _setup_gpio(self, watering_pin):
        self.waterPinIn = watering_pin
        GPIO.setup(self.waterPinIn, GPIO.IN)
        GPIO.add_event_detect(self.waterPinIn, GPIO.BOTH, self._watering, bouncetime=1)

    def _change_status(self, status=STATUS_DEFAULT):
        self._status = status

    def _get_status(self):
        return self._status

    def _watering(self, channel):
        print 'come'
        print 'begin time:' + str(time.time())
        if mutex.acquire(1):
            gpio_input = GPIO.input(channel)
            print 'come in ' + str(gpio_input)
            if gpio_input == 1 and self._get_status() != STATUS_WATERING:
                self._change_status(STATUS_WATERING)
                for func in self.watering_funcs:
                    func()
            elif gpio_input == 0 and self._get_status() != STATUS_DEFAULT:
                if self._get_status() != STATUS_DEFAULT:
                    self._change_status(STATUS_DEFAULT)
                    for func in self.stop_watering_funcs:
                        func()
            print 'release'
            mutex.release()
            print 'end time:' + str(time.time())

    def start(self, pin=27):
        self._setup_gpio(pin)
        self._watering(pin)

        print 'watering robo started'
        try:
            while True:
                time.sleep(0.5)
        except KeyboardInterrupt:
            print 'bye bye'
        self.stop()

    def stop(self):
        GPIO.remove_event_detect(self.waterPinIn)

    def execute(self, func):
        func(self)

    def detected_soil_is_dry_then(self, func_name=None):
        func = self._assemable_func(func_name)
        if func is None:
            return
        self.watering_funcs.append(func)

    def detected_soil_is_wet_then(self, func_name=None):
        func = self._assemable_func(func_name)
        if func is None:
            return
        self.stop_watering_funcs.append(func)

    def _assemable_func(self, func_name):
        func = None
        if func_name == Command.TURN_MOTOR_CLOCK_WISE:
            func = functools.partial(self.turn_with_angel, 60)
        elif func_name == Command.TURN_MOTOR_ANTI_CLOCK_WISE:
            func = functools.partial(self.turn_with_angel, -60)
        elif func_name == Command.LIGHT_ON:
            func = functools.partial(self.light_on, 22)
        elif func_name == Command.LIGHT_OFF:
            func = functools.partial(self.light_off, 22)
        elif func_name == Command.BEEP:
            func = functools.partial(self.beep, 17, 1)
        elif func_name == Command.MUTE:
            func = functools.partial(self.mute, 17)
        elif func_name == Command.START_PUMP:
            func = functools.partial(self.start_pump, 2)
        elif func_name == Command.STOP_PUMP:
            func = functools.partial(self.stop_pump, 2)

        return func


robo = WateringRobo()
