from motor import Motor
from wateringRoboInterface import WateringRoboInterface
from wateringRobo import robo


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
        self.motor.turnWithAngel(60)

    def stop_watering(self):
        WateringRoboInterface.stop_watering(self)
        """
        input your code below
        """
        self.motor.turnWithAngel(-60)

    def exit(self):
        WateringRoboInterface.exit(self)
        """
        input your code below
        """
        self.motor.stop()


if __name__ == "__main__":
    robo.start(27, MainCallback())
