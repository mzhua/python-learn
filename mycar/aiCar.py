# coding=utf-8
"""
智能寻迹小车
"""
from car import Car
from sensor.ledLight import LedLight

_frontLight = LedLight()


class AICar(Car):
    def __init__(self):
        Car.__init__(self)

    def lightenFrontLight(self):
        _frontLight.light(True)
        print 'front light on'

    def cleanup(self):
        Car.cleanup(self)
    
    print 'index' + 0 + 1

