import RPi.GPIO as GPIO


class RPiBase:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
