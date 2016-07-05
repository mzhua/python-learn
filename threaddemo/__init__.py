from backgroundtask import BackgroundTask

bgt = BackgroundTask()

bgt.startLoop()

try:
    text = input()
    print str(text)
except KeyboardInterrupt:
    pass
