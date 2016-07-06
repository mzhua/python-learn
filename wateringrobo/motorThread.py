import math
import threading
import time

import RPi.GPIO as GPIO

DIRECTION_CLOCK_WISE = 0
DIRECTION_ANTI_CLOCK_WISE = 1


class MotorThread(threading.Thread):
    def __init__(self, pins=None, angel=30):
        threading.Thread.__init__(self)
        if pins is None:
            pins = [2, 3, 4, 14]
        self.pins = pins
        self.angel = angel
        self.turnedCounts = 0
        self.exitFlag = 0
        self._rollDirection = DIRECTION_CLOCK_WISE

        GPIO.setmode(GPIO.BCM)
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    def run(self):
        loop_counts = math.trunc(math.fabs(self.angel) / 360 * 2048)
        index = 0  # pin index
        try:
            while loop_counts > 0 and not self.exitFlag:
                if self.angel > 0:
                    self._rollDirection = DIRECTION_CLOCK_WISE
                    # print 'roll' + str(loop_counts)
                    if index > 0:
                        GPIO.output(self.pins[index - 1], 0)
                    else:
                        GPIO.output(self.pins[3], 0)
                    GPIO.output(self.pins[index], 1)
                    index += 1
                    if index > 3:
                        index = 0
                else:
                    self._rollDirection = DIRECTION_ANTI_CLOCK_WISE
                    # print 'roll' + str(loop_counts)
                    if index < 3:
                        GPIO.output(self.pins[index + 1], 0)
                    else:
                        GPIO.output(self.pins[0], 0)
                    GPIO.output(self.pins[index], 1)
                    index -= 1
                    if index < 0:
                        index = 3
                time.sleep(0.002)
                loop_counts -= 1
                self.turnedCounts += 1
        except AttributeError:
            pass

    def clear(self):
        self.exitFlag = 1

    def get_turned_counts(self):
        return self.turnedCounts
