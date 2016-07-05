import RPi.GPIO as GPIO
import time

from motor import Motor

waterPinIn = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(waterPinIn, GPIO.IN)

motor = Motor([2, 3, 4, 14])

STATUS_DEFAULT = 0
STATUS_WATERING = 1

_status = STATUS_DEFAULT


def _changeStatus(status=STATUS_DEFAULT):
    global _status
    _status = status


def _getStatus():
    global _status
    return _status


def watering(channel):
    if GPIO.input(channel) == 1:
        if _getStatus() == STATUS_WATERING:
            return
        else:
            _changeStatus(STATUS_WATERING)
        motor.turnWithAngel(30)
        print 'start'
    else:
        if _getStatus() == STATUS_DEFAULT:
            return
        else:
            _changeStatus(STATUS_DEFAULT)
        motor.turnWithAngel(-30)
        print 'stop'


GPIO.add_event_detect(waterPinIn, GPIO.BOTH, watering)

loop = True
try:
    while loop:
        time.sleep(5)
        # text = raw_input()
        # if text == 'f':
        #     motor.turnWithAngel(30)
        # elif text == 'b':
        #     motor.turnWithAngel(-30)
except KeyboardInterrupt:
    loop = False

GPIO.remove_event_detect(waterPinIn)
