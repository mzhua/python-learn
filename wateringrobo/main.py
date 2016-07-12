import robo.sensor.motor
import robo.sensor.beeper
import robo.sensor.ledLight
from robo.command import Command
from robo.wateringRobo import robo



def instruction(robo):
    robo.detected_soil_is_dry_then(Command.TURN_MOTOR_CLOCK_WISE)
    robo.detected_soil_is_dry_then(Command.BEEP)
    robo.detected_soil_is_dry_then(Command.LIGHT_ON)
    robo.detected_soil_is_wet_then(Command.TURN_MOTOR_ANTI_CLOCK_WISE)
    robo.detected_soil_is_wet_then(Command.LIGHT_OFF)
    robo.detected_soil_is_wet_then(Command.MUTE)
    robo.start(27)


robo.execute(instruction)
