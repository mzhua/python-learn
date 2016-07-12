import time
import functools
from command import Command
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
                commond_str = raw_input()
                if commond_str == 'w':
                    for func in self.watering_funcs:
                        func()
                elif commond_str == 's':
                    for func in self.stop_watering_funcs:
                        func()
                elif commond_str == 'exit':
                    break
                time.sleep(5)
        except KeyboardInterrupt:
            print 'bye bye'
        self.stop()

    def stop(self):
        GPIO.remove_event_detect(self.waterPinIn)
        GPIO.cleanup()

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

        return func

robo = WateringRobo()