# coding=utf-8
"""
马达
"""
import RPi.GPIO as GPIO
import time

_isRunning = False
pins = [2, 3, 4, 14]


class Motor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pins[0], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(pins[1], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(pins[2], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(pins[3], GPIO.OUT, initial=GPIO.LOW)

    def turnWithSpeed(self, clockwise=True, speed=5):
        """
        :param clockwise:
        :param speed: circle per second
        :return:
        """
        if self._isMotorStarted():
            print 'motor turn speed: ' + str(speed) + ' in ' + ('clockwise' if clockwise else 'anticlockwise')
            loop = True
            global pins
            index = 0
            try:
                while loop:

                    if clockwise:
                        if index > 0:
                            GPIO.output(pins[index - 1], 0)
                        else:
                            GPIO.output(pins[3], 0)
                        GPIO.output(pins[index], 1)

                        index += 1
                        if index > 3:
                            index = 0
                    else:
                        if index < 3:
                            GPIO.output(pins[index + 1], 0)
                        else:
                            GPIO.output(pins[0], 0)
                        GPIO.output(pins[index], 1)

                        index -= 1
                        if index < 0:
                            index = 3

                    time.sleep(0.002)

            except KeyboardInterrupt:
                loop = False

        return _isRunning

    def _isMotorStarted(self):
        if not _isRunning:
            print 'please start the motor first'
        return True
