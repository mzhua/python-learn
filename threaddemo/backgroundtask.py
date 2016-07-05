#!/usr/bin/python
# -*- coding: UTF-8 -*-
import thread
import threading
import time

exitFlag = 0


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "Starting " + self.name
        self.print_time(self.name, self.counter, 10)
        print "Exiting " + self.name

    def print_time(self, threadName, delay, counter):
        while counter:
            if exitFlag:
                thread.exit()
                break
            time.sleep(delay)
            print "%s: %s" % (threadName, time.ctime(time.time()))
            counter -= 1

    def clear(self):
        print 'clear'
        global exitFlag
        exitFlag = 1
