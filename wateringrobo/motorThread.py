import math
import threading
import time

import RPi.GPIO as GPIO

DIRECTION_CLOCK_WISE = 0
DIRECTION_ANTI_CLOCK_WISE = 1

_rollDirection = DIRECTION_CLOCK_WISE


class MotorThread(threading.Thread):
    def __init__(self, pins=None, angel=30):
        threading.Thread.__init__(self)
        if pins is None:
            pins = []
        self.pins = pins
        self.angel = angel
        self.turnedCounts = 0
        self.exitFlag = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pins[0], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(pins[1], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(pins[2], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(pins[3], GPIO.OUT, initial=GPIO.LOW)

    def run(self):
        print "Starting " + self.name

        loop_counts = math.trunc(math.fabs(self.angel) / 360 * 4096)
        index = 0  # pin index
        global _rollDirection
        while loop_counts > 0 and not self.exitFlag:
            if self.angel > 0:
                _rollDirection = DIRECTION_CLOCK_WISE
                if index > 0:
                    GPIO.output(self.pins[index - 1], 0)
                else:
                    GPIO.output(self.pins[3], 0)
                GPIO.output(self.pins[index], 1)
                index += 1
                if index > 3:
                    index = 0
            else:
                _rollDirection = DIRECTION_ANTI_CLOCK_WISE
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

        print "Exiting " + self.name

    def clear(self):
        self.exitFlag = 1

    def getTurnedCounts(self):
        return self.turnedCounts
