# coding=utf-8
import math
import thread
import time

import RPi.GPIO as GPIO

DIRECTION_CLOCK_WISE = 0
DIRECTION_ANTI_CLOCK_WISE = 1

_isRunning = False
_rollDirection = DIRECTION_CLOCK_WISE
pins = []
_thread = None


# 4096个脉冲信号则转一圈(360°)
class Motor:
    def __init__(self, pin=None):
        if pin is None:
            pin = []
        GPIO.setmode(GPIO.BCM)
        global pins
        pins = pin
        GPIO.setup(pins[0], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(pins[1], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(pins[2], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(pins[3], GPIO.OUT, initial=GPIO.LOW)

    def _turnOnMotor(self, angel=30):
        self._changeMotorStatus(True)
        print 'motor turn angel: ' + str(angel) + ' in ' + ('clockwise' if angel > 0 else 'anticlockwise')
        loop_counts = math.trunc(math.fabs(angel) / 360 * 4096)
        global pins
        index = 0  # pin index
        global _rollDirection
        while loop_counts > 0:
            if angel > 0:
                _rollDirection = DIRECTION_CLOCK_WISE
                if index > 0:
                    GPIO.output(pins[index - 1], 0)
                else:
                    GPIO.output(pins[3], 0)
                GPIO.output(pins[index], 1)
                index += 1
                if index > 3:
                    index = 0
            else:
                _rollDirection = DIRECTION_ANTI_CLOCK_WISE
                if index < 3:
                    GPIO.output(pins[index + 1], 0)
                else:
                    GPIO.output(pins[0], 0)
                GPIO.output(pins[index], 1)
                index -= 1
                if index < 0:
                    index = 3
            time.sleep(0.002)
            loop_counts -= 1
        self._changeMotorStatus(False)

    def turnWithAngel(self, angel=30, instantChange=True):
        if angel == 0:
            return
        """
        :param angel: the angel want to turn,set negative to turn anticlockwise and set positive to turn clockwise
        :return:
        """
        if not self.isMotorRunning() or instantChange:
            thread.exit()
            thread.start_new_thread(self._turnOnMotor(angel), ("Motor-1", 2,))
        else:
            print 'the motor is running, please wait a moment'
        return self.isMotorRunning()

    def isMotorRunning(self):
        global _isRunning
        return _isRunning

    def getMotorRollDirection(self):
        global _rollDirection
        return _rollDirection

    def _changeMotorStatus(self, status=False):
        global _isRunning
        _isRunning = status
