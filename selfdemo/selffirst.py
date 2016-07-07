class SelfFirst(object):
    def _init_self_first(self):
        self.aa = 9

    def just_print(self):
        self._init_self_first()
        print str(self.aa)
