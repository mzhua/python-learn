# coding=utf-8
import atexit
import threading
import time

import RPi.GPIO as GPIO

atexit.register(GPIO.cleanup)

p = None


class RoboHandThread(threading.Thread):
    def __init__(self, pin=None):
        threading.Thread.__init__(self)
        GPIO.setmode(GPIO.BCM)
        global p
        p = GPIO.PWM(pin, 50)
        p.start(0)
        time.sleep(0.5)

    def run(self):
        super(RoboHandThread, self).run()
