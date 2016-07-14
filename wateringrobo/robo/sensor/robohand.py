from sensorBase import SensorBase
from ..util.equip_to import equip_to
from ..wateringRobo import WateringRobo


@equip_to(WateringRobo)
class RoboHand(SensorBase):
    def _setup(self):
        super(RoboHand, self)._setup()
