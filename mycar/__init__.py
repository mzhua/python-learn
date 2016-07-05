from aiCar import AICar


def start():
    print 'type up/down/left/right to control the car, and type stop to stop the car, and type off to power off the car'
    c = AICar()
    loop = True
    try:
        while loop:

            command = raw_input()
            if command == 'stop':
                c.stop()
            elif command == 'up':
                c.forward()
            elif command == 'down':
                c.backward()
            elif command == 'left':
                c.left()
            elif command == 'right':
                c.right()
            elif command == 'off':
                c.poweroff()
            elif command == 'beep':
                c.beep()
            else:
                print 'invalid command'
    except KeyboardInterrupt:
        pass


start()


def sensor():
    return None
