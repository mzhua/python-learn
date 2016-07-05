# coding=utf-8
"""
汽车
"""
import sys
import RPi.GPIO as GPIO
from rpiBase import RPiBase
from sensor.motor import Motor

_engine = Motor()


class Car(RPiBase):
    def __init__(self):
        RPiBase.__init__(self)

    def forward(self):
        _engine.turnWithSpeed(True, 10)
        print 'car forward'

    def backward(self):
        _engine.turnWithSpeed(False, 5)
        print 'car goback'

    def left(self):
        print 'car turn left'

    def right(self):
        print 'car turn right'

    def start(self):
        _engine.start()
        print 'car started'

    def stop(self):
        _engine.stop()
        print 'car stopped'

    def poweroff(self):
        _engine.powoff()
        print 'car power off, good bye'
        GPIO.cleanup()
        sys.exit(0)

    def beep(self):
        print 'car beep'

    def cleanup(self):
        print 'cleanup'
