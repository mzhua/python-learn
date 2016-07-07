from ..equip_to import equip_to
from ..first.first import First
from ..third.third import Third

demo = 7
third = Third()


@equip_to(First)
class Second(object):
    def __init__(self, tt=3):
        print 'second init'
        self.test = tt

    def just_print(self):
        print 'I\'m second and test is ' + str(self.test)

    def get_demo(self):
        print 'demo is ' + str(demo)

    def call_third(self):
        third.hello_third()
