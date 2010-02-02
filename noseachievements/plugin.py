from nose.plugins import Plugin


class Achievements(Plugin):
    def __init__(self):
        Plugin.__init__(self)
        self.data = {}

