from motor import Motor
from wateringInterface import WateringInterface
from wateringRobo import WateringRobo

motor = Motor([2, 3, 4, 14])


class MainCallback(WateringInterface):
    def __init__(self):
        WateringInterface.__init__(self)

    def start_watering(self):
        WateringInterface.start_watering(self)
        global motor
        motor.turnWithAngel(60)

    def stop_watering(self):
        WateringInterface.stop_watering(self)
        global motor
        motor.turnWithAngel(-60)


if __name__ == "__main__":
    wateringrobo = WateringRobo(27)

    wateringrobo.start(MainCallback())

