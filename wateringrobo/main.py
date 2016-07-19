import robo.sensor.motor
import robo.sensor.pump
import robo.sensor.beeper
import robo.sensor.ledLight
from robo.command import Command
from robo.wateringRobo import robo


def instruction(robo):
    robo.detected_soil_is_dry_then(Command.LIGHT_ON)
    robo.detected_soil_is_dry_then(Command.START_PUMP)
    robo.detected_soil_is_dry_then(Command.BEEP)
    robo.detected_soil_is_wet_then(Command.LIGHT_OFF)
    robo.detected_soil_is_wet_then(Command.MUTE)
    robo.detected_soil_is_wet_then(Command.STOP_PUMP)
    robo.start(27)


robo.execute(instruction)
