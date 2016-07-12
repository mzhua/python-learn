# coding=utf-8
from motorThread import MotorThread
from sensorBase import SensorBase
from ..util.equip_to import equip_to
from ..wateringRobo import WateringRobo


@equip_to(WateringRobo)
class Motor(SensorBase):
    def _setup(self):
        self.pins = None
        self._is_running = False
        self.motor_thread = None

    def _motor_thread_exit_callback(self):
        self._change_motor_status(False)

    def turn_with_angel(self, angel=30, pins=None, instant_change=False):
        """
        :param pins:
        :param instant_change: change the turn direction immediately
        :param angel: the angel want to turn,set negative to turn anticlockwise and set positive to turn clockwise
        :return:
        """

        if angel == 0:
            return

        self.pins = pins

        if not self._is_motor_running() or instant_change:
            self._change_motor_status(True)

            print 'motor turn angel: ' + str(angel) + ' in ' + (
                'clockwise' if angel > 0 else 'anticlockwise')

            if self.motor_thread is not None:
                self.motor_thread.clear()
                self.motor_thread = None

            self.motor_thread = MotorThread(self.pins, angel, self._motor_thread_exit_callback)
            self.motor_thread.start()

        else:
            print 'the motor is running, please wait a moment'

    def stop(self):
        if self.motor_thread is not None:
            self.motor_thread.clear()
            self.motor_thread = None

    def _is_motor_running(self):
        return self._is_running

    def _change_motor_status(self, status=False):
        self._is_running = status
