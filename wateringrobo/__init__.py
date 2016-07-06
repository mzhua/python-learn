from motor import Motor
from wateringRobo import robo
import functools


def instruction(robo):
    mt = Motor([2, 3, 4, 14])
    robo.do_what_when_need_to_watering([functools.partial(mt.turn_with_angel, 60)])
    robo.do_what_when_need_to_stop_watering([functools.partial(mt.turn_with_angel, - 60)])
    robo.start(27)

robo.execute(instruction)
