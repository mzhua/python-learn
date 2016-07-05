class PrintTestClass(object):
    def __init__(self, f):
        print('inside PrintTestClass init')
        f()

    def __call__(self):
        print('inside PrintTestClass call')
