from wateringInterface import WateringInterface


class Another:
    def __init__(self):
        pass

    def callbackfn(self, callback):
        if not isinstance(callback, WateringInterface):
            print 'not the WateringInterface'
            return
        callback.start_watering()
