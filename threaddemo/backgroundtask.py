import time
import thread


class BackgroundTask:
    def __init__(self):
        pass

    def _loop(self):
        i = 0
        while i < 5000:
            time.sleep(2)
            i += 1
            print str(i)

    def startLoop(self):
        thread.start_new_thread(self._loop(), ("Thread-1", 2,))
