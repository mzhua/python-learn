# coding=utf-8
from motorThread import MotorThread

_isRunning = False
motorThread = None


class Motor:
    def __init__(self, pins=None):
        if pins is None:
            pins = []
        self.pins = pins

    def turnWithAngel(self, angel=30, instantChange=True):
        """
        :param instantChange: change the turn direction immediately
        :param angel: the angel want to turn,set negative to turn anticlockwise and set positive to turn clockwise
        :return:
        """
        if angel == 0:
            return

        if not self.isMotorRunning() or instantChange:
            self._changeMotorStatus(True)

            print 'motor turn angel: ' + str(angel) + ' in ' + (
                'clockwise' if angel > 0 else 'anticlockwise')

            global motorThread
            if motorThread is not None:
                motorThread.clear()

            motorThread = MotorThread(self.pins, angel)
            motorThread.start()

            self._changeMotorStatus(False)
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
