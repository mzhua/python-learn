from motor import Motor
from wateringRoboInterface import WateringRoboInterface
from wateringRobo import robo
import functools


class MainCallback(WateringRoboInterface):
    def __init__(self):
        WateringRoboInterface.__init__(self)
        """
        initial your device below
        """
        self.motor = Motor([2, 3, 4, 14])

    def start_watering(self):
        WateringRoboInterface.start_watering(self)
        """
        input your code below
        """
        self.motor.turn_with_angel(60)

    def stop_watering(self):
        WateringRoboInterface.stop_watering(self)
        """
        input your code below
        """
        self.motor.turn_with_angel(-60)

    def exit(self):
        WateringRoboInterface.exit(self)
        """
        input your code below
        """
        self.motor.stop()


def instruction(robo):
    mt = Motor([2, 3, 4, 14])
    robo.do_what_when_need_to_watering([functools.partial(mt.turn_with_angel, 60)])
    robo.do_what_when_need_to_stop_watering([functools.partial(mt.turn_with_angel, - 60)])
    robo.start(27, MainCallback())

    # if __name__ == "__main__":


robo.execute(instruction)
