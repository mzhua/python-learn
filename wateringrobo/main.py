import functools
import robo.sensor.motor
import robo.sensor.beeper
import robo.sensor.ledLight
from robo.wateringRobo import WateringRobo


def instruction(robo):
    robo.do_what_when_need_to_watering([functools.partial(robo.turn_with_angel, 60),functools.partial(robo.beep,17),functools.partial(robo.light,True,22)])
    robo.do_what_when_need_to_stop_watering([functools.partial(robo.turn_with_angel, - 60),functools.partial(robo.light,False,22)])
    robo.start(27)


WateringRobo().execute(instruction)
