from another import Another
from wateringInterface import WateringInterface


class Hello(WateringInterface):
    def stop_watering(self):
        WateringInterface.stop_watering(self)
        print 'stop_watering'

    def start_watering(self):
        WateringInterface.start_watering(self)
        print 'start_watering'

    def __init__(self):
        WateringInterface.__init__(self)


another = Another()
another.callbackfn(Hello())
