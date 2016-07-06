# coding=utf-8
from motorThread import MotorThread

motorThread = None


class Motor:
    def __init__(self, pins=None):
        if pins is None:
            pins = []
        self.pins = pins
        self._isRunning = False

    def turnWithAngel(self, angel=30, instant_change=True):
        """
        :param instant_change: change the turn direction immediately
        :param angel: the angel want to turn,set negative to turn anticlockwise and set positive to turn clockwise
        :return:
        """
        if angel == 0:
            return

        if not self.is_motor_running() or instant_change:
            self._change_motor_status(True)

            print 'motor turn angel: ' + str(angel) + ' in ' + (
                'clockwise' if angel > 0 else 'anticlockwise')

            global motorThread
            if motorThread is not None:
                motorThread.clear()

            motorThread = MotorThread(self.pins, angel)
            motorThread.start()

            self._change_motor_status(False)
        else:
            print 'the motor is running, please wait a moment'

        return self.is_motor_running()

    def is_motor_running(self):
        return self._isRunning

    def _change_motor_status(self, status=False):
        self._isRunning = status
