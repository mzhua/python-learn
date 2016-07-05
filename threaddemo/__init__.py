# coding=utf-8
import time

from backgroundtask import myThread

thread1 = myThread(1, "Thread-1", 1)
# 开启线程

print 'hello'
try:
    while True:
        text = raw_input()
        if text == 'start':
            thread1.start()
        elif text == 'clear':
            thread1.clear()
except KeyboardInterrupt:
    pass

print "Exiting Main Thread"
